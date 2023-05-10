from typing import Dict

import numpy as np

from rubiks_cube_checker.cube import RubiksCube, CubeFace


def test_rotate(scrambled_cube_state: Dict[CubeFace, np.ndarray], move: str) -> None:
    cube = RubiksCube(faces=scrambled_cube_state)
    # TODO: fill in
