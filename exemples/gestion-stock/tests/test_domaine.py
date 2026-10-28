"""Tests du domaine. Chaque test cite les règles (R-xx) et scénarios (S-xx) qu'il prouve."""
import dataclasses
import random
from datetime import datetime, timezone

import pytest

from stock.domaine import (
    Piece,
    PieceArchivee,
    Quantite,
    QuantiteInvalide,
    Sens,
    StockBas,
    StockInsuffisant,
)

T0 = datetime(2026, 3, 3, 10, 0, tzinfo=timezone.utc)


def piece_avec_stock(stock: int, seuil: int = 0) -> Piece:
    piece = Piece("VIS-M6", seuil_alerte=seuil)
    if stock:
        piece.entrer("init", Quantite(stock), T0)
    return piece


# S-01, R-07
def test_S01_entree_augmente_le_stock():
    piece = piece_avec_stock(0)
    piece.entrer("e1", Quantite(10), T0)
    assert piece.stock == 10


# S-02, R-04, R-07
def test_S02_sortie_normale():
    piece = piece_avec_stock(10)
    piece.sortir("s1", Quantite(4), T0)
    assert piece.stock == 6


# S-03, R-04 : contre-exemple
def test_R04_sortie_superieure_au_stock_refusee():
    piece = piece_avec_stock(10)
    with pytest.raises(StockInsuffisant, match="Stock insuffisant : 10 disponibles"):
        piece.sortir("s1", Quantite(12), T0)
    assert piece.stock == 10


# S-05, R-04 : la limite exacte est acceptée
def test_S05_sortie_jusqu_a_zero():
    piece = piece_avec_stock(10)
    piece.sortir("s1", Quantite(10), T0)
    assert piece.stock == 0


# S-04, R-02
@pytest.mark.parametrize("valeur", [0, -3, 2.5, "4", True])
def test_R02_quantite_invalide_refusee(valeur):
    with pytest.raises(QuantiteInvalide):
        Quantite(valeur)


# S-06, R-05 : une alerte au passage du seuil, pas de seconde alerte en dessous
def test_R05_alerte_une_seule_fois_au_passage_du_seuil():
    piece = piece_avec_stock(6, seuil=5)
    assert piece.sortir("s1", Quantite(2), T0) == [StockBas("VIS-M6", 4, 5)]
    assert piece.sortir("s2", Quantite(1), T0) == []


# S-08, R-06
def test_R06_piece_archivee_refuse_tout_mouvement():
    piece = piece_avec_stock(10)
    piece.archiver()
    with pytest.raises(PieceArchivee, match="La pièce VIS-M6 est archivée"):
        piece.entrer("e1", Quantite(5), T0)
    with pytest.raises(PieceArchivee):
        piece.sortir("s1", Quantite(1), T0)


# S-09, R-08 : idempotence
def test_R08_meme_requete_enregistree_une_seule_fois():
    piece = piece_avec_stock(10)
    piece.sortir("s1", Quantite(4), T0)
    piece.sortir("s1", Quantite(4), T0)
    assert piece.stock == 6
    assert len([m for m in piece.mouvements if m.sens is Sens.SORTIE]) == 1


# S-12, R-09, R-07 : correction par mouvement inverse ; l'historique ne se modifie pas
def test_R09_correction_par_mouvement_inverse():
    piece = piece_avec_stock(10)
    piece.sortir("erreur", Quantite(4), T0)
    piece.entrer("correction", Quantite(4), T0)
    assert piece.stock == 10
    assert [m.id_requete for m in piece.mouvements] == ["init", "erreur", "correction"]
    with pytest.raises(dataclasses.FrozenInstanceError):
        piece.mouvements[1].quantite = Quantite(1)
    assert isinstance(piece.mouvements, tuple)


# R-04, R-07 : test de propriété sur 2 000 suites de mouvements aléatoires
def test_R04_R07_propriete_stock_jamais_negatif_et_egal_a_la_somme():
    hasard = random.Random(2026)
    for essai in range(2000):
        piece = Piece("P-1")
        attendu = 0
        for i in range(hasard.randint(1, 30)):
            q = hasard.randint(1, 20)
            if hasard.random() < 0.5:
                piece.entrer(f"{essai}-{i}", Quantite(q), T0)
                attendu += q
            else:
                try:
                    piece.sortir(f"{essai}-{i}", Quantite(q), T0)
                    attendu -= q
                except StockInsuffisant:
                    pass
            assert piece.stock >= 0
        assert piece.stock == attendu
