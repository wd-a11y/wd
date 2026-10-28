"""Tests de wd-check. Lancer avec : python -m pytest outils/wd-check"""
from pathlib import Path

import pytest

from wd_check import analyser, formater_matrice, main


def projet(tmp_path: Path, fichiers: dict) -> Path:
    for nom, contenu in fichiers.items():
        chemin = tmp_path / nom
        chemin.parent.mkdir(parents=True, exist_ok=True)
        chemin.write_text(contenu, encoding="utf-8")
    return tmp_path


REGLES = "| Id | Règle |\n| --- | --- |\n| R-01 | Le stock ne devient jamais négatif |\n"


def test_regle_citee_par_un_test_sans_erreur(tmp_path):
    p = projet(tmp_path, {
        "docs/B-regles.md": REGLES,
        "tests/test_stock.py": "# R-01\ndef test_stock():\n    pass\n",
    })
    rapport = analyser(p)
    assert rapport.erreurs == []
    assert "R-01" in rapport.definitions


def test_regle_sans_test_est_une_erreur(tmp_path):
    p = projet(tmp_path, {"docs/B-regles.md": REGLES})
    rapport = analyser(p)
    assert any(e.startswith("R-01 n'est cité par aucun test") for e in rapport.erreurs)


def test_citation_dun_identifiant_non_defini(tmp_path):
    p = projet(tmp_path, {
        "docs/B-regles.md": REGLES,
        "docs/B-scenarios.feature": "Scénario: S-01 Sortie refusée (R-01, R-15)\n",
        "tests/test_stock.py": "# R-01 S-01\n",
    })
    rapport = analyser(p)
    assert any(e.startswith("R-15 est cité mais défini nulle part") for e in rapport.erreurs)


def test_double_definition(tmp_path):
    p = projet(tmp_path, {
        "docs/B-regles.md": REGLES + "### R-01 — doublon\n",
        "tests/test_stock.py": "# R-01\n",
    })
    rapport = analyser(p)
    assert any(e.startswith("R-01 est défini 2 fois") for e in rapport.erreurs)


def test_identifiant_sans_tiret_dans_un_nom_de_test(tmp_path):
    p = projet(tmp_path, {
        "docs/B-regles.md": REGLES,
        "tests/test_stock.py": "def test_R01_sortie_refusee():\n    pass\n",
    })
    assert analyser(p).erreurs == []


def test_scenario_sans_test_avertit_puis_bloque_en_strict(tmp_path):
    fichiers = {
        "docs/B-regles.md": REGLES,
        "docs/B-scenarios.feature": "Scénario: S-01 Sortie refusée (R-01)\n",
        "tests/test_stock.py": "# R-01\n",
    }
    p = projet(tmp_path, fichiers)
    rapport = analyser(p)
    assert rapport.erreurs == []
    assert any(a.startswith("S-01") for a in rapport.avertissements)
    assert any(e.startswith("S-01") for e in analyser(p, strict=True).erreurs)


def test_le_code_et_la_matrice_ne_definissent_rien(tmp_path):
    p = projet(tmp_path, {
        "docs/B-regles.md": REGLES,
        "docs/tracabilite.md": "| R-01 | règle |\n",
        "docs/bilans/2026-01-01.md": "| B-01 | 3 | 0 |\n",
        "src/stock.py": "# R-01 appliquée ici\n",
        "tests/test_stock.py": "# R-01\n",
    })
    rapport = analyser(p)
    assert len(rapport.definitions["R-01"]) == 1
    assert "B-01" not in rapport.definitions
    assert "R-01" in rapport.citations["code"]


def test_matrice(tmp_path):
    p = projet(tmp_path, {
        "docs/B-regles.md": REGLES,
        "tests/test_stock.py": "# R-01\n",
    })
    matrice = formater_matrice(analyser(p))
    assert "| R-01 | règle | `docs/B-regles.md` | — | `tests/test_stock.py` | — |" in matrice


def test_codes_de_sortie(tmp_path, capsys):
    p = projet(tmp_path, {"docs/B-regles.md": REGLES})
    assert main([str(p)]) == 1
    (p / "tests").mkdir()
    (p / "tests" / "test_stock.py").write_text("# R-01\n", encoding="utf-8")
    assert main([str(p)]) == 0
    assert main([str(p / "inexistant")]) == 2
    assert "Résultat" in capsys.readouterr().out
