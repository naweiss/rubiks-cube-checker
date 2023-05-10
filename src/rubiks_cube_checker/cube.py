from __future__ import annotations
from typing import Dict, Optional, List, Union
import copy
import enum

import numpy as np


class CubeFace(str, enum.Enum):
    UP = 'U'
    DOWN = 'D'
    FRONT = 'F'
    BACK = 'B'
    LEFT = 'L'
    RIGHT = 'R'


class RubiksCube:
    def __init__(self, faces: Optional[Dict[CubeFace, np.ndarray]] = None) -> None:
        if faces is not None:
            self.faces: Dict[CubeFace, np.ndarray] = copy.deepcopy(faces)
        else:
            self.faces: Dict[CubeFace, np.ndarray] = {
                CubeFace.UP: np.full((3, 3), 'w'),
                CubeFace.DOWN: np.full((3, 3), 'y'),
                CubeFace.FRONT: np.full((3, 3), 'g'),
                CubeFace.BACK: np.full((3, 3), 'b'),
                CubeFace.LEFT: np.full((3, 3), 'o'),
                CubeFace.RIGHT: np.full((3, 3), 'r')
            }

    def rotate(self, face: Union[CubeFace, str]) -> None:
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

    def __eq__(self, other: RubiksCube) -> bool:
        return all(np.array_equal(self.faces[face], other.faces[face]) for face in self.faces.keys())
