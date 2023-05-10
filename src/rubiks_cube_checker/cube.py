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


# TODO: add type hints
class RubiksCube:
    def __init__(self, faces = None):
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

    def rotate(self, face):
        self.faces[face] = np.rot90(self.faces[face], k=-1)
        if face == 'U':
            temp = self.faces[CubeFace.LEFT][0].copy()
            self.faces[CubeFace.LEFT][0] = self.faces[CubeFace.FRONT][0]
            self.faces[CubeFace.FRONT][0] = self.faces[CubeFace.RIGHT][0]
            self.faces[CubeFace.RIGHT][0] = self.faces[CubeFace.BACK][0]
            self.faces[CubeFace.BACK][0] = temp
        elif face == 'D':
            temp = self.faces[CubeFace.BACK][2].copy()
            self.faces[CubeFace.BACK][2] = self.faces[CubeFace.RIGHT][2]
            self.faces[CubeFace.RIGHT][2] = self.faces[CubeFace.FRONT][2]
            self.faces[CubeFace.FRONT][2] = self.faces[CubeFace.LEFT][2]
            self.faces[CubeFace.LEFT][2] = temp
        elif face == 'F':
            temp = self.faces[CubeFace.DOWN][0].copy()
            self.faces[CubeFace.DOWN][0] = np.flip(self.faces[CubeFace.RIGHT][:, 0])
            self.faces[CubeFace.RIGHT][:, 0] = self.faces[CubeFace.UP][2]
            self.faces[CubeFace.UP][2] = np.flip(self.faces[CubeFace.LEFT][:, 2])
            self.faces[CubeFace.LEFT][:, 2] = temp
        elif face == 'B':
            temp = self.faces[CubeFace.RIGHT][:, 2].copy()
            self.faces[CubeFace.RIGHT][:, 2] = np.flip(self.faces[CubeFace.DOWN][2])
            self.faces[CubeFace.DOWN][2] = self.faces[CubeFace.LEFT][:, 0]
            self.faces[CubeFace.LEFT][:, 0] = np.flip(self.faces[CubeFace.UP][0])
            self.faces[CubeFace.UP][0] = temp
        elif face == 'L':
            temp = self.faces[CubeFace.FRONT][:, 0].copy()
            self.faces[CubeFace.FRONT][:, 0] = self.faces[CubeFace.UP][:, 0]
            self.faces[CubeFace.UP][:, 0] = np.flip(self.faces[CubeFace.BACK][:, 2])
            self.faces[CubeFace.BACK][:, 2] = np.flip(self.faces[CubeFace.DOWN][:, 0])
            self.faces[CubeFace.DOWN][:, 0] = temp
        elif face == 'R':
            temp = self.faces[CubeFace.DOWN][:, 2].copy()
            self.faces[CubeFace.DOWN][:, 2] = np.flip(self.faces[CubeFace.BACK][:, 0])
            self.faces[CubeFace.BACK][:, 0] = np.flip(self.faces[CubeFace.UP][:, 2])
            self.faces[CubeFace.UP][:, 2] = self.faces[CubeFace.FRONT][:, 2]
            self.faces[CubeFace.FRONT][:, 2] = temp
        else:
            raise ValueError(f'Invalid face {face}')

    @staticmethod
    def _split_move(move):
        if move.endswith("'"):
            times = 3
        elif move.endswith('2'):
            times = 2
        elif len(move) == 1:
            times = 1
        else:
            raise ValueError(f'Invalid move {move}')
        return move[0], times

    def do_move(self, move):
        if len(move) > 2:
            raise ValueError(f'Invalid move {move}')

        move, times = self._split_move(move)
        for _ in range(times):
            self.rotate(move)

    def __str__(self):
        def _stringify_numpy_array(array, prefix = ''):
            return '\n'.join(prefix + ' '.join(row) for row in array)

        middle = np.concatenate([self.faces[CubeFace.LEFT], self.faces[CubeFace.FRONT], self.faces[CubeFace.RIGHT], self.faces[CubeFace.BACK]], axis=1)
        return '\n'.join([
            _stringify_numpy_array(self.faces[CubeFace.UP], prefix='      '),
            _stringify_numpy_array(middle),
            _stringify_numpy_array(self.faces[CubeFace.DOWN], prefix='      '),
        ])

    def __eq__(self, other):
        return all(np.array_equal(self.faces[face], other.faces[face]) for face in self.faces.keys())
