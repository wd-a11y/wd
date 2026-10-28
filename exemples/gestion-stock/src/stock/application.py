"""Application : un cas d'usage par action. Droits, verrou, domaine, enregistrement, événements."""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Callable

from .domaine import ErreurMetier, Piece, Quantite

ROLES_MOUVEMENT = {"magasinier", "responsable"}  # R-03
ROLES_GESTION = {"responsable"}  # R-10


class AccesRefuse(ErreurMetier):
    pass


class PieceInconnue(ErreurMetier):
    pass


class ReferenceDejaUtilisee(ErreurMetier):
    pass


def _maintenant() -> datetime:
    return datetime.now(timezone.utc)


class ServiceStock:
    def __init__(
        self,
        depot,
        publier: Callable[[object], None] = lambda evenement: None,
        horloge: Callable[[], datetime] = _maintenant,
    ) -> None:
        self._depot = depot
        self._publier = publier
        self._horloge = horloge

    def creer_piece(self, role: str, reference: str, seuil_alerte: int = 0) -> None:
        self._autoriser(role, ROLES_GESTION)
        with self._depot.verrou(reference):
            if self._depot.existe(reference):  # R-01
                raise ReferenceDejaUtilisee(f"La référence {reference} existe déjà")
            self._depot.enregistrer(Piece(reference, seuil_alerte))

    def archiver_piece(self, role: str, reference: str) -> None:
        self._autoriser(role, ROLES_GESTION)
        with self._depot.verrou(reference):
            piece = self._charger(reference)
            piece.archiver()
            self._depot.enregistrer(piece)

    def entrer(self, role: str, reference: str, quantite: int, id_requete: str) -> None:
        self._mouvement(role, reference, quantite, id_requete, entree=True)

    def sortir(self, role: str, reference: str, quantite: int, id_requete: str) -> None:
        self._mouvement(role, reference, quantite, id_requete, entree=False)

    def stock(self, reference: str) -> int:
        return self._charger(reference).stock

    def _mouvement(self, role, reference, quantite, id_requete, entree: bool) -> None:
        self._autoriser(role, ROLES_MOUVEMENT)
        q = Quantite(quantite)  # R-02, vérifiée à la frontière
        with self._depot.verrou(reference):
            piece = self._charger(reference)
            action = piece.entrer if entree else piece.sortir
            evenements = action(id_requete, q, self._horloge())
            self._depot.enregistrer(piece)
        for evenement in evenements:
            self._publier(evenement)

    def _charger(self, reference: str) -> Piece:
        piece = self._depot.charger(reference)
        if piece is None:
            raise PieceInconnue(f"Pièce inconnue : {reference}")
        return piece

    @staticmethod
    def _autoriser(role: str, roles: set) -> None:
        if role not in roles:
            raise AccesRefuse("Accès non autorisé")
