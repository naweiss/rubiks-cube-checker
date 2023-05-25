from __future__ import annotations
from typing import Dict, Optional, List, Tuple
import copy
import enum

import numpy as np

from rubiks_cube_checker.math import permutation_parity


class CubeFace(str, enum.Enum):
    UP = 'U'
    DOWN = 'D'
    FRONT = 'F'
    BACK = 'B'
    LEFT = 'L'
    RIGHT = 'R'


class RubiksCube:
    def __init__(self, faces: Optional[Dict[str, np.ndarray]] = None) -> None:
        self.faces: Dict[str, np.ndarray]

        if faces is not None:
            self.faces = copy.deepcopy(faces)
        else:
            self.faces = {
                CubeFace.UP: np.full((3, 3), 'w'),
                CubeFace.DOWN: np.full((3, 3), 'y'),
                CubeFace.FRONT: np.full((3, 3), 'g'),
                CubeFace.BACK: np.full((3, 3), 'b'),
                CubeFace.LEFT: np.full((3, 3), 'o'),
                CubeFace.RIGHT: np.full((3, 3), 'r')
            }

    def rotate(self, face: str) -> None:
        self.faces[face] = np.rot90(self.faces[face], k=-1)
        if face == CubeFace.UP:
            temp = self.faces[CubeFace.LEFT][0].copy()
            self.faces[CubeFace.LEFT][0] = self.faces[CubeFace.FRONT][0]
            self.faces[CubeFace.FRONT][0] = self.faces[CubeFace.RIGHT][0]
            self.faces[CubeFace.RIGHT][0] = self.faces[CubeFace.BACK][0]
            self.faces[CubeFace.BACK][0] = temp
        elif face == CubeFace.DOWN:
            temp = self.faces[CubeFace.BACK][2].copy()
            self.faces[CubeFace.BACK][2] = self.faces[CubeFace.RIGHT][2]
            self.faces[CubeFace.RIGHT][2] = self.faces[CubeFace.FRONT][2]
            self.faces[CubeFace.FRONT][2] = self.faces[CubeFace.LEFT][2]
            self.faces[CubeFace.LEFT][2] = temp
        elif face == CubeFace.FRONT:
            temp = self.faces[CubeFace.DOWN][0].copy()
            self.faces[CubeFace.DOWN][0] = np.flip(self.faces[CubeFace.RIGHT][:, 0])
            self.faces[CubeFace.RIGHT][:, 0] = self.faces[CubeFace.UP][2]
            self.faces[CubeFace.UP][2] = np.flip(self.faces[CubeFace.LEFT][:, 2])
            self.faces[CubeFace.LEFT][:, 2] = temp
        elif face == CubeFace.BACK:
            temp = self.faces[CubeFace.RIGHT][:, 2].copy()
            self.faces[CubeFace.RIGHT][:, 2] = np.flip(self.faces[CubeFace.DOWN][2])
            self.faces[CubeFace.DOWN][2] = self.faces[CubeFace.LEFT][:, 0]
            self.faces[CubeFace.LEFT][:, 0] = np.flip(self.faces[CubeFace.UP][0])
            self.faces[CubeFace.UP][0] = temp
        elif face == CubeFace.LEFT:
            temp = self.faces[CubeFace.FRONT][:, 0].copy()
            self.faces[CubeFace.FRONT][:, 0] = self.faces[CubeFace.UP][:, 0]
            self.faces[CubeFace.UP][:, 0] = np.flip(self.faces[CubeFace.BACK][:, 2])
            self.faces[CubeFace.BACK][:, 2] = np.flip(self.faces[CubeFace.DOWN][:, 0])
            self.faces[CubeFace.DOWN][:, 0] = temp
        elif face == CubeFace.RIGHT:
            temp = self.faces[CubeFace.DOWN][:, 2].copy()
            self.faces[CubeFace.DOWN][:, 2] = np.flip(self.faces[CubeFace.BACK][:, 0])
            self.faces[CubeFace.BACK][:, 0] = np.flip(self.faces[CubeFace.UP][:, 2])
            self.faces[CubeFace.UP][:, 2] = self.faces[CubeFace.FRONT][:, 2]
            self.faces[CubeFace.FRONT][:, 2] = temp
        else:
            raise ValueError(f'Invalid face {face}')

    @staticmethod
    def _split_move(move: str) -> List[str]:
        if len(move) > 2:
            raise ValueError(f'Invalid move {move}')
        elif move.endswith("'"):
            times = 3
        elif move.endswith('2'):
            times = 2
        else:
            times = 1
        return [move[0]] * times

    def do_move(self, move: str) -> None:
        moves = self._split_move(move)
        for move in moves:
            self.rotate(move)

    def _get_edge_pieces(self) -> List[Tuple[str, str]]:
        return [
            (self.faces[CubeFace.UP][0, 1], self.faces[CubeFace.BACK][0, 1]),
            (self.faces[CubeFace.UP][1, 2], self.faces[CubeFace.RIGHT][0, 1]),
            (self.faces[CubeFace.UP][2, 1], self.faces[CubeFace.FRONT][0, 1]),
            (self.faces[CubeFace.UP][1, 0], self.faces[CubeFace.LEFT][0, 1]),
            (self.faces[CubeFace.DOWN][0, 1], self.faces[CubeFace.FRONT][2, 1]),
            (self.faces[CubeFace.DOWN][1, 2], self.faces[CubeFace.RIGHT][2, 1]),
            (self.faces[CubeFace.DOWN][2, 1], self.faces[CubeFace.BACK][2, 1]),
            (self.faces[CubeFace.DOWN][1, 0], self.faces[CubeFace.LEFT][2, 1]),
            (self.faces[CubeFace.FRONT][1, 2], self.faces[CubeFace.RIGHT][1, 0]),
            (self.faces[CubeFace.FRONT][1, 0], self.faces[CubeFace.LEFT][1, 2]),
            (self.faces[CubeFace.BACK][1, 2], self.faces[CubeFace.LEFT][1, 0]),
            (self.faces[CubeFace.BACK][1, 0], self.faces[CubeFace.RIGHT][1, 2]),
        ]

    def _get_corner_pieces(self) -> List[Tuple[str, str, str]]:
        return [
            (self.faces[CubeFace.UP][0, 0], self.faces[CubeFace.BACK][0, 2], self.faces[CubeFace.LEFT][0, 0]),
            (self.faces[CubeFace.UP][0, 2], self.faces[CubeFace.RIGHT][0, 2], self.faces[CubeFace.BACK][0, 0]),
            (self.faces[CubeFace.UP][2, 0], self.faces[CubeFace.LEFT][0, 2], self.faces[CubeFace.FRONT][0, 0]),
            (self.faces[CubeFace.UP][2, 2], self.faces[CubeFace.FRONT][0, 2], self.faces[CubeFace.RIGHT][0, 0]),
            (self.faces[CubeFace.DOWN][0, 0], self.faces[CubeFace.FRONT][2, 0], self.faces[CubeFace.LEFT][2, 2]),
            (self.faces[CubeFace.DOWN][0, 2], self.faces[CubeFace.RIGHT][2, 0], self.faces[CubeFace.FRONT][2, 2]),
            (self.faces[CubeFace.DOWN][2, 0], self.faces[CubeFace.LEFT][2, 0], self.faces[CubeFace.BACK][2, 2]),
            (self.faces[CubeFace.DOWN][2, 2], self.faces[CubeFace.BACK][2, 0], self.faces[CubeFace.RIGHT][2, 2]),
        ]

    @staticmethod
    def _get_edge_parity(edge: Tuple[str, str]) -> int:
        if edge[0] == 'w' or edge[0] == 'y':
            return 0
        if edge[0] == 'g' or edge[0] == 'b':
            if edge[1] == 'r' or edge[1] == 'o':
                return 0
        return 1

    @staticmethod
    def _get_corner_parity(corner: Tuple[str, str, str]) -> int:
        if corner[0] == 'w' or corner[0] == 'y':
            return 0
        if corner[1] == 'w' or corner[1] == 'y':
            return 1
        return 2

    def _total_edge_parity(self) -> int:
        return sum([self._get_edge_parity(edge) for edge in self._get_edge_pieces()])

    def _total_corner_parity(self) -> int:
        return sum([self._get_corner_parity(corner) for corner in self._get_corner_pieces()])

    def _total_edge_permutation_parity(self) -> int:
        return permutation_parity(
            current_state=self._get_edge_pieces(),
            solved_state=RubiksCube()._get_edge_pieces()
        )

    def _total_corner_permutation_parity(self) -> int:
        return permutation_parity(
            current_state=self._get_corner_pieces(),
            solved_state=RubiksCube()._get_corner_pieces()
        )

    def is_solvable(self) -> bool:
        return (
                self._total_edge_parity() % 2 == 0 and
                self._total_corner_parity() % 3 == 0 and
                self._total_edge_permutation_parity() == self._total_corner_permutation_parity()
        )

    def __str__(self) -> str:
        def _stringify_numpy_array(array: np.ndarray, prefix: str = '') -> str:
            return '\n'.join(prefix + ' '.join(row) for row in array)

        middle = np.concatenate([self.faces[CubeFace.LEFT], self.faces[CubeFace.FRONT], self.faces[CubeFace.RIGHT],
                                 self.faces[CubeFace.BACK]], axis=1)
        return '\n'.join([
            _stringify_numpy_array(self.faces[CubeFace.UP], prefix='      '),
            _stringify_numpy_array(middle),
            _stringify_numpy_array(self.faces[CubeFace.DOWN], prefix='      '),
        ])

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, RubiksCube):
            return NotImplemented
        return all(np.array_equal(self.faces[face], other.faces[face]) for face in self.faces.keys())
