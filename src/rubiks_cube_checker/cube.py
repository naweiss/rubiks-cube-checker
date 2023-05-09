from copy import deepcopy

import numpy as np


# TODO: add type hints
class RubiksCube:
    def __init__(self, faces=None):
        if faces is not None:
            self.faces = deepcopy(faces)
        else:
            self.faces = {
                'U': np.full((3, 3), 'w'),
                'D': np.full((3, 3), 'y'),
                'F': np.full((3, 3), 'g'),
                'B': np.full((3, 3), 'b'),
                'L': np.full((3, 3), 'o'),
                'R': np.full((3, 3), 'r')
            }

    def rotate(self, face):
        self.faces[face] = np.rot90(self.faces[face], k=-1)
        if face == 'U':
            temp = self.faces['L'][0].copy()
            self.faces['L'][0] = self.faces['F'][0]
            self.faces['F'][0] = self.faces['R'][0]
            self.faces['R'][0] = self.faces['B'][0]
            self.faces['B'][0] = temp
        elif face == 'D':
            temp = self.faces['B'][2].copy()
            self.faces['B'][2] = self.faces['R'][2]
            self.faces['R'][2] = self.faces['F'][2]
            self.faces['F'][2] = self.faces['L'][2]
            self.faces['L'][2] = temp
        elif face == 'F':
            temp = self.faces['D'][0].copy()
            self.faces['D'][0] = np.flip(self.faces['R'][:, 0])
            self.faces['R'][:, 0] = self.faces['U'][2]
            self.faces['U'][2] = np.flip(self.faces['L'][:, 2])
            self.faces['L'][:, 2] = temp
        elif face == 'B':
            temp = self.faces['R'][:, 2].copy()
            self.faces['R'][:, 2] = np.flip(self.faces['D'][2])
            self.faces['D'][2] = self.faces['L'][:, 0]
            self.faces['L'][:, 0] = np.flip(self.faces['U'][0])
            self.faces['U'][0] = temp
        elif face == 'L':
            temp = self.faces['F'][:, 0].copy()
            self.faces['F'][:, 0] = self.faces['U'][:, 0]
            self.faces['U'][:, 0] = np.flip(self.faces['B'][:, 2])
            self.faces['B'][:, 2] = np.flip(self.faces['D'][:, 0])
            self.faces['D'][:, 0] = temp
        elif face == 'R':
            temp = self.faces['D'][:, 2].copy()
            self.faces['D'][:, 2] = np.flip(self.faces['B'][:, 0])
            self.faces['B'][:, 0] = np.flip(self.faces['U'][:, 2])
            self.faces['U'][:, 2] = self.faces['F'][:, 2]
            self.faces['F'][:, 2] = temp
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
        def _stringify_numpy_array(array, prefix=''):
            return '\n'.join(prefix + ' '.join(row) for row in array)

        middle = np.concatenate([self.faces['L'], self.faces['F'], self.faces['R'], self.faces['B']], axis=1)
        return '\n'.join([
            _stringify_numpy_array(self.faces['U'], prefix='      '),
            _stringify_numpy_array(middle),
            _stringify_numpy_array(self.faces['D'], prefix='      '),
        ])

    def __eq__(self, other):
        return all(np.array_equal(self.faces[face], other.faces[face]) for face in self.faces.keys())
