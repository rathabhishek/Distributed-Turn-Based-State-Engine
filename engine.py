"""Headless Tic-Tac-Toe game engine suitable for microservices.

Provides a minimal `GameEngine` class with no UI dependencies so it can be
imported by `FastAPI` or other frameworks.
"""

from typing import List, Optional, Dict, Any


class GameEngine:
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self.TTT: List[List[Optional[str]]] = [[None] * 3 for _ in range(3)]
        self.XO: str = 'x'
        self.winner: Optional[str] = None
        self.draw: bool = False

    def get_state(self) -> Dict[str, Any]:
        return {
            'board': self.TTT,
            'next': self.XO,
            'winner': self.winner,
            'draw': self.draw,
        }

    def make_move(self, row: int, col: int) -> Dict[str, Any]:
        """Place a mark on the board.

        row and col are 1-based (1..3). Raises ValueError for invalid moves.
        Returns the new state dict.
        """
        if self.winner or self.draw:
            raise ValueError('Game already finished; reset to play again')

        if not (1 <= row <= 3 and 1 <= col <= 3):
            raise ValueError('row and col must be between 1 and 3')

        if self.TTT[row - 1][col - 1] is not None:
            raise ValueError('Cell already occupied')

        self.TTT[row - 1][col - 1] = self.XO
        # toggle
        self.XO = 'o' if self.XO == 'x' else 'x'
        self._check_win()
        return self.get_state()

    def _check_win(self) -> None:
        b = self.TTT
        # rows
        for r in range(3):
            if b[r][0] is not None and b[r][0] == b[r][1] == b[r][2]:
                self.winner = b[r][0]
                return
        # cols
        for c in range(3):
            if b[0][c] is not None and b[0][c] == b[1][c] == b[2][c]:
                self.winner = b[0][c]
                return
        # diagonals
        if b[0][0] is not None and b[0][0] == b[1][1] == b[2][2]:
            self.winner = b[0][0]
            return
        if b[0][2] is not None and b[0][2] == b[1][1] == b[2][0]:
            self.winner = b[0][2]
            return

        # draw
        if all(all(cell is not None for cell in row) for row in b):
            self.draw = True


__all__ = ['GameEngine']
