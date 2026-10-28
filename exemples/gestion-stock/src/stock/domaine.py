"""Domaine : les règles du stock. Aucune dépendance vers la base, l'écran ou le réseau."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class ErreurMetier(Exception):
    """Refus prévu par une règle métier."""


class QuantiteInvalide(ErreurMetier):
    pass


class StockInsuffisant(ErreurMetier):
    pass


class PieceArchivee(ErreurMetier):
    pass


class Sens(Enum):
    ENTREE = "entree"
    SORTIE = "sortie"


@dataclass(frozen=True)
class Quantite:
    """Objet-valeur. R-02 : un entier strictement positif."""

    valeur: int

    def __post_init__(self) -> None:
        if isinstance(self.valeur, bool) or not isinstance(self.valeur, int) or self.valeur <= 0:
            raise QuantiteInvalide("Une quantité doit être un entier strictement positif")


@dataclass(frozen=True)
class Mouvement:
    """Entrée ou sortie. Immuable : R-09."""

    id_requete: str
    sens: Sens
    quantite: Quantite
    horodatage: datetime


@dataclass(frozen=True)
class StockBas:
    """Événement publié quand une sortie fait passer le stock sous le seuil (R-05)."""

    reference: str
    stock: int
    seuil: int


class Piece:
    """Entité, racine d'agrégat : une pièce et ses mouvements changent ensemble."""

    def __init__(self, reference: str, seuil_alerte: int = 0) -> None:
        if not reference or len(reference) > 30:
            raise ValueError("La référence doit faire de 1 à 30 caractères")
        if seuil_alerte < 0:
            raise ValueError("Le seuil d'alerte ne peut pas être négatif")
        self.reference = reference
        self.seuil_alerte = seuil_alerte
        self.archivee = False
        self._mouvements: list[Mouvement] = []

    @property
    def stock(self) -> int:
        """R-07 : entrées moins sorties ; les mouvements font foi."""
        total = 0
        for m in self._mouvements:
            total += m.quantite.valeur if m.sens is Sens.ENTREE else -m.quantite.valeur
        return total

    @property
    def mouvements(self) -> tuple[Mouvement, ...]:
        """R-09 : l'historique se lit, il ne se modifie pas."""
        return tuple(self._mouvements)

    def entrer(self, id_requete: str, quantite: Quantite, quand: datetime) -> list:
        return self._enregistrer(Mouvement(id_requete, Sens.ENTREE, quantite, quand))

    def sortir(self, id_requete: str, quantite: Quantite, quand: datetime) -> list:
        return self._enregistrer(Mouvement(id_requete, Sens.SORTIE, quantite, quand))

    def archiver(self) -> None:
        self.archivee = True

    def _enregistrer(self, mouvement: Mouvement) -> list:
        if self.archivee:  # R-06
            raise PieceArchivee(f"La pièce {self.reference} est archivée")
        if any(m.id_requete == mouvement.id_requete for m in self._mouvements):  # R-08
            return []
        avant = self.stock
        if mouvement.sens is Sens.SORTIE and mouvement.quantite.valeur > avant:  # R-04
            raise StockInsuffisant(f"Stock insuffisant : {avant} disponibles")
        self._mouvements.append(mouvement)
        apres = self.stock
        if mouvement.sens is Sens.SORTIE and avant >= self.seuil_alerte > apres:  # R-05
            return [StockBas(self.reference, apres, self.seuil_alerte)]
        return []
