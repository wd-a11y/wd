#!/usr/bin/env python3
"""wd-check : vérifie la traçabilité d'un projet qui suit la méthode WD.

Il lit les identifiants (B-, F-, H-, R-, S-, T-, D-, M-) dans le dossier docs/,
les tests et le code, puis signale :
  - les identifiants définis deux fois ;
  - les identifiants cités mais définis nulle part ;
  - les règles R-xx qu'aucun test ne cite ;
  - (avertissement) les scénarios S-xx qu'aucun test ne cite ;
  - (avertissement) les besoins, fonctionnalités et menaces jamais cités.

Usage :
    python wd_check.py CHEMIN_DU_PROJET [--docs docs] [--strict] [--matrice FICHIER]

Code de sortie : 0 sans erreur, 1 avec erreurs, 2 si le projet est introuvable.
Aucune dépendance : Python 3.9 ou plus récent suffit.
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

NATURES = {
    "B": "besoin",
    "F": "fonctionnalité",
    "H": "hypothèse",
    "R": "règle",
    "S": "scénario",
    "T": "test",
    "D": "décision",
    "M": "menace",
}
ORDRE = "BFHRSMDT"
# Les identifiants T- sont libres : ils ne sont pas vérifiés.
VERIFIES = set("BFHRSDM")

_ID = r"[BFHRSTDM]-\d{2,3}"
RE_ID = re.compile(rf"(?<![A-Za-z0-9-])({_ID})(?![0-9])")
# Dans un nom de test, l'identifiant peut s'écrire sans tiret : test_R04_sortie_refusee
RE_ID_SANS_TIRET = re.compile(r"(?<=_)([BFHRSTDM])(\d{2,3})(?=_|\b)")
RE_DEFINITIONS = [
    re.compile(rf"^\s*\|\s*\**({_ID})(?![0-9])"),  # | R-04 | ...
    re.compile(rf"^\s*#+\s*\**({_ID})(?![0-9])"),  # ### R-04 ...
    re.compile(rf"^\s*(?:[-*]\s+)?\*\*({_ID})(?![0-9])"),  # **R-04** ou - **R-04**
    re.compile(rf"^\s*>\s*\*\*({_ID})(?![0-9])"),  # > **R-04**
    re.compile(
        rf"^\s*(?:Scénario|Scenario|Plan du scénario|Scenario Outline)\s*:\s*({_ID})(?![0-9])"
    ),
]

EXTENSIONS = {
    ".md", ".feature", ".txt", ".py", ".js", ".mjs", ".ts", ".tsx", ".jsx", ".java",
    ".kt", ".cs", ".go", ".rs", ".rb", ".php", ".c", ".h", ".cpp", ".hpp", ".cc",
    ".swift", ".dart", ".scala", ".ino", ".sql", ".yml", ".yaml", ".json", ".toml",
}
DOSSIERS_IGNORES = {
    ".git", "node_modules", ".venv", "venv", "__pycache__", ".pytest_cache",
    "dist", "build", "target", ".idea", ".vscode",
}
DOSSIERS_TESTS = {"tests", "test", "spec", "specs", "__tests__"}
# Fichiers de docs/ qui citent sans définir.
DOCS_SANS_DEFINITION = {"tracabilite.md"}
DOSSIERS_DOCS_SANS_DEFINITION = {"bilans"}


@dataclass(frozen=True)
class Position:
    fichier: str
    ligne: int

    def __str__(self) -> str:
        return f"{self.fichier}:{self.ligne}"


@dataclass
class Rapport:
    projet: Path
    definitions: dict = field(default_factory=lambda: defaultdict(list))
    citations: dict = field(
        default_factory=lambda: {"docs": defaultdict(list), "tests": defaultdict(list), "code": defaultdict(list)}
    )
    erreurs: list = field(default_factory=list)
    avertissements: list = field(default_factory=list)


def _cle_tri(identifiant: str) -> tuple:
    prefixe, numero = identifiant.split("-")
    return (ORDRE.index(prefixe), int(numero))


def _categorie(chemin_relatif: Path, docs: str) -> str:
    parties = chemin_relatif.parts
    if parties and parties[0] == docs:
        return "docs"
    nom = chemin_relatif.name
    if (
        any(p in DOSSIERS_TESTS for p in parties[:-1])
        or nom.startswith("test_")
        or "_test." in nom
        or ".test." in nom
        or ".spec." in nom
    ):
        return "tests"
    return "code"


def _fichiers(projet: Path):
    for chemin in sorted(projet.rglob("*")):
        relatif = chemin.relative_to(projet)
        if any(p in DOSSIERS_IGNORES for p in relatif.parts):
            continue
        if chemin.is_file() and chemin.suffix.lower() in EXTENSIONS:
            yield chemin, relatif


def _definit(chemin_relatif: Path, docs: str) -> bool:
    if chemin_relatif.name in DOCS_SANS_DEFINITION:
        return False
    if any(p in DOSSIERS_DOCS_SANS_DEFINITION for p in chemin_relatif.parts[1:-1]):
        return False
    return chemin_relatif.suffix.lower() in {".md", ".feature"}


def analyser(projet: Path, docs: str = "docs", strict: bool = False) -> Rapport:
    """Lit le projet et retourne le rapport de traçabilité."""
    projet = Path(projet)
    rapport = Rapport(projet=projet)

    for chemin, relatif in _fichiers(projet):
        categorie = _categorie(relatif, docs)
        peut_definir = categorie == "docs" and _definit(relatif, docs)
        texte = chemin.read_text(encoding="utf-8", errors="replace")
        nom = relatif.as_posix()

        for numero, ligne in enumerate(texte.splitlines(), start=1):
            position = Position(nom, numero)
            defini_ici = None
            if peut_definir:
                for motif in RE_DEFINITIONS:
                    trouve = motif.match(ligne)
                    if trouve:
                        defini_ici = trouve.group(1)
                        rapport.definitions[defini_ici].append(position)
                        break

            vus = [m.group(1) for m in RE_ID.finditer(ligne)]
            if categorie == "tests":
                vus += [f"{m.group(1)}-{m.group(2)}" for m in RE_ID_SANS_TIRET.finditer(ligne)]
            deja_compte_definition = False
            for identifiant in vus:
                if identifiant == defini_ici and not deja_compte_definition:
                    deja_compte_definition = True
                    continue
                rapport.citations[categorie][identifiant].append(position)

    _verifier(rapport, strict)
    return rapport


def _verifier(rapport: Rapport, strict: bool) -> None:
    definis = rapport.definitions
    tests = rapport.citations["tests"]

    for identifiant in sorted(definis, key=_cle_tri):
        positions = definis[identifiant]
        if len(positions) > 1:
            lieux = ", ".join(str(p) for p in positions)
            rapport.erreurs.append(f"{identifiant} est défini {len(positions)} fois ({lieux})")

    premiere_citation = {}
    for table in rapport.citations.values():
        for identifiant, positions in table.items():
            premiere_citation.setdefault(identifiant, positions[0])
    cites = set(premiere_citation)
    for identifiant, position in premiere_citation.items():
        if identifiant[0] in VERIFIES and identifiant not in definis:
            rapport.erreurs.append(f"{identifiant} est cité mais défini nulle part ({position})")

    for identifiant in sorted(definis, key=_cle_tri):
        prefixe = identifiant[0]
        lieu = definis[identifiant][0]
        if prefixe == "R" and identifiant not in tests:
            rapport.erreurs.append(f"{identifiant} n'est cité par aucun test (défini en {lieu})")
        elif prefixe == "S" and identifiant not in tests:
            rapport.avertissements.append(
                f"{identifiant} n'est cité par aucun test (défini en {lieu})"
            )
        elif prefixe in {"B", "F", "M"} and identifiant not in cites:
            rapport.avertissements.append(
                f"{identifiant} ({NATURES[prefixe]}) n'est cité nulle part (défini en {lieu})"
            )

    rapport.erreurs = sorted(set(rapport.erreurs), key=lambda t: (_cle_tri(t.split()[0]), t))
    if strict:
        rapport.erreurs += rapport.avertissements
        rapport.avertissements = []


def formater_matrice(rapport: Rapport) -> str:
    """Retourne la matrice de traçabilité au format Markdown."""

    def fichiers(table: dict, identifiant: str) -> str:
        noms = sorted({p.fichier for p in table.get(identifiant, [])})
        return ", ".join(f"`{n}`" for n in noms) if noms else "—"

    lignes = [
        "# Traçabilité",
        "",
        "Fichier généré par `wd-check`. Ne pas le modifier à la main.",
        "",
        "| Id | Nature | Défini dans | Cité dans les docs | Cité dans les tests | Cité dans le code |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for identifiant in sorted(rapport.definitions, key=_cle_tri):
        defini = ", ".join(sorted({f"`{p.fichier}`" for p in rapport.definitions[identifiant]}))
        lignes.append(
            f"| {identifiant} | {NATURES[identifiant[0]]} | {defini} | "
            f"{fichiers(rapport.citations['docs'], identifiant)} | "
            f"{fichiers(rapport.citations['tests'], identifiant)} | "
            f"{fichiers(rapport.citations['code'], identifiant)} |"
        )
    return "\n".join(lignes) + "\n"


def formater_resume(rapport: Rapport) -> str:
    compte = defaultdict(int)
    for identifiant in rapport.definitions:
        compte[identifiant[0]] += 1
    detail = ", ".join(
        f"{compte[p]} {NATURES[p]}{'s' if compte[p] > 1 else ''}" for p in ORDRE if compte[p]
    )
    lignes = [f"wd-check — {rapport.projet}", f"Définis : {detail or 'aucun identifiant'}"]
    lignes += [f"ERREUR      {e}" for e in rapport.erreurs]
    lignes += [f"ATTENTION   {a}" for a in rapport.avertissements]
    lignes.append(
        f"Résultat : {len(rapport.erreurs)} erreur(s), {len(rapport.avertissements)} avertissement(s)."
    )
    return "\n".join(lignes)


def main(arguments=None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except (OSError, ValueError):
            pass
    parseur = argparse.ArgumentParser(
        prog="wd-check", description="Vérifie la traçabilité d'un projet suivant la méthode WD."
    )
    parseur.add_argument("projet", nargs="?", default=".", help="dossier du projet (défaut : .)")
    parseur.add_argument("--docs", default="docs", help="dossier des livrables (défaut : docs)")
    parseur.add_argument("--strict", action="store_true", help="traiter les avertissements comme des erreurs")
    parseur.add_argument("--matrice", metavar="FICHIER", help="écrire la matrice de traçabilité dans ce fichier")
    options = parseur.parse_args(arguments)

    projet = Path(options.projet)
    if not (projet / options.docs).is_dir():
        print(f"wd-check : dossier introuvable : {projet / options.docs}", file=sys.stderr)
        return 2

    rapport = analyser(projet, docs=options.docs, strict=options.strict)
    print(formater_resume(rapport))
    if options.matrice:
        Path(options.matrice).write_text(formater_matrice(rapport), encoding="utf-8")
        print(f"Matrice écrite dans {options.matrice}")
    return 1 if rapport.erreurs else 0


if __name__ == "__main__":
    sys.exit(main())
