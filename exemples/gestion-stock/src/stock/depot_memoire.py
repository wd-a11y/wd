"""Infrastructure : conserve les pièces en mémoire, avec un verrou par pièce (D-01)."""
from __future__ import annotations

import threading
from contextlib import contextmanager

from .domaine import Piece


class DepotMemoire:
    def __init__(self) -> None:
        self._pieces: dict[str, Piece] = {}
        self._verrous: dict[str, threading.Lock] = {}
        self._verrou_general = threading.Lock()

    @contextmanager
    def verrou(self, reference: str):
        """Une seule opération à la fois sur une même pièce."""
        with self._verrou_general:
            verrou = self._verrous.setdefault(reference, threading.Lock())
        with verrou:
            yield

    def existe(self, reference: str) -> bool:
        return reference in self._pieces

    def charger(self, reference: str) -> Piece | None:
        return self._pieces.get(reference)

    def enregistrer(self, piece: Piece) -> None:
        self._pieces[piece.reference] = piece
