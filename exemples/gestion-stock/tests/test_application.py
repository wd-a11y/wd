"""Tests des cas d'usage : droits, unicité, concurrence, événements."""
import threading

import pytest

from stock.application import AccesRefuse, PieceInconnue, ReferenceDejaUtilisee, ServiceStock
from stock.depot_memoire import DepotMemoire
from stock.domaine import StockBas, StockInsuffisant


@pytest.fixture
def service():
    publies = []
    s = ServiceStock(DepotMemoire(), publier=publies.append)
    s.publies = publies
    s.creer_piece("responsable", "VIS-M6", seuil_alerte=5)
    s.entrer("magasinier", "VIS-M6", 10, "init")
    return s


# S-10, R-03
def test_R03_visiteur_ne_peut_pas_sortir(service):
    with pytest.raises(AccesRefuse):
        service.sortir("visiteur", "VIS-M6", 4, "s1")
    assert service.stock("VIS-M6") == 10


# S-13, R-10
def test_R10_magasinier_ne_cree_pas_de_piece(service):
    with pytest.raises(AccesRefuse):
        service.creer_piece("magasinier", "VIS-M8")


# S-11, R-01
def test_R01_reference_en_double_refusee(service):
    with pytest.raises(ReferenceDejaUtilisee):
        service.creer_piece("responsable", "VIS-M6")


# R-06, R-10 : archivage par le responsable
def test_R06_archivage_bloque_les_mouvements(service):
    service.archiver_piece("responsable", "VIS-M6")
    with pytest.raises(Exception, match="archivée"):
        service.entrer("magasinier", "VIS-M6", 5, "e1")


# R-05 : l'événement est publié vers l'extérieur
def test_R05_stock_bas_publie(service):
    service.sortir("magasinier", "VIS-M6", 6, "s1")
    assert service.publies == [StockBas("VIS-M6", 4, 5)]


def test_piece_inconnue(service):
    with pytest.raises(PieceInconnue):
        service.sortir("magasinier", "INCONNUE", 1, "s1")


# S-07, R-04 : deux sorties de 6 au même instant sur un stock de 10
def test_S07_deux_sorties_simultanees_une_seule_reussit():
    for _ in range(50):
        s = ServiceStock(DepotMemoire())
        s.creer_piece("responsable", "VIS-M6")
        s.entrer("magasinier", "VIS-M6", 10, "init")
        depart = threading.Barrier(2)
        resultats = []

        def sortir(id_requete):
            depart.wait()
            try:
                s.sortir("magasinier", "VIS-M6", 6, id_requete)
                resultats.append("acceptée")
            except StockInsuffisant:
                resultats.append("refusée")

        fils = [threading.Thread(target=sortir, args=(f"s{i}",)) for i in range(2)]
        for f in fils:
            f.start()
        for f in fils:
            f.join()
        assert sorted(resultats) == ["acceptée", "refusée"]
        assert s.stock("VIS-M6") == 4
