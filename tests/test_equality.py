from typing import Dict

import numpy as np

from rubiks_cube_checker.cube import RubiksCube, CubeFace


def test_equality_sanity(scrambled_cube_state: Dict[str, np.ndarray]) -> None:
    cube_a = RubiksCube(faces=scrambled_cube_state)
    cube_b = RubiksCube(faces=scrambled_cube_state)
    assert cube_a == cube_b


def test_inequality_sanity(scrambled_cube_state: Dict[str, np.ndarray]) -> None:
    solved_cube = RubiksCube()
    scrambled_cube = RubiksCube(faces=scrambled_cube_state)
    assert solved_cube != scrambled_cube


def test_inequality(scrambled_cube_state: Dict[str, np.ndarray], move: str) -> None:
    cube_a = RubiksCube(faces=scrambled_cube_state)
    cube_b = RubiksCube(faces=scrambled_cube_state)
    cube_b.rotate(move)
    assert cube_a != cube_b


def test_equality(scrambled_cube_state: Dict[str, np.ndarray], move: str) -> None:
    cube_a = RubiksCube(faces=scrambled_cube_state)
    cube_a.rotate(move)

    cube_b = RubiksCube(faces=scrambled_cube_state)
    cube_b.rotate(move)

    assert cube_a == cube_b
