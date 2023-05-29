from __future__ import annotations

import random
from typing import TYPE_CHECKING, Dict

from rubiks_cube_checker.cube import CubeFace, RubiksCube

if TYPE_CHECKING:
    from numpy.typing import NDArray


def test_solvable_sanity() -> None:
    cube = RubiksCube()
    assert cube.is_solvable()


def test_solvable_scrambled(scrambled_cube_state: Dict[str, NDArray]) -> None:
    cube = RubiksCube(faces=scrambled_cube_state)
    assert cube.is_solvable()


def test_solvable_complex() -> None:
    cube = RubiksCube()
    for _ in range(100):
        for move in random.choice(["U", "D", "R", "L", "F", "B"]):
            cube.do_move(move)
        assert cube.is_solvable()


def test_not_solvable_twisted_corner() -> None:
    cube = RubiksCube()

    # Twist single corner
    temp = cube.faces[CubeFace.DOWN][0, 2]
    cube.faces[CubeFace.DOWN][0, 2] = cube.faces[CubeFace.RIGHT][2, 0]
    cube.faces[CubeFace.RIGHT][2, 0] = cube.faces[CubeFace.FRONT][2, 2]
    cube.faces[CubeFace.FRONT][2, 2] = temp

    assert not cube.is_solvable()

    # Twist same corner again
    temp = cube.faces[CubeFace.DOWN][0, 2]
    cube.faces[CubeFace.DOWN][0, 2] = cube.faces[CubeFace.RIGHT][2, 0]
    cube.faces[CubeFace.RIGHT][2, 0] = cube.faces[CubeFace.FRONT][2, 2]
    cube.faces[CubeFace.FRONT][2, 2] = temp

    assert not cube.is_solvable()


def test_not_solvable_multiple_twisted_corners() -> None:
    cube = RubiksCube()

    # Twist 2 different corners
    temp = cube.faces[CubeFace.DOWN][0, 2]
    cube.faces[CubeFace.DOWN][0, 2] = cube.faces[CubeFace.RIGHT][2, 0]
    cube.faces[CubeFace.RIGHT][2, 0] = cube.faces[CubeFace.FRONT][2, 2]
    cube.faces[CubeFace.FRONT][2, 2] = temp
    temp = cube.faces[CubeFace.DOWN][2, 0]
    cube.faces[CubeFace.DOWN][2, 0] = cube.faces[CubeFace.LEFT][2, 0]
    cube.faces[CubeFace.LEFT][2, 0] = cube.faces[CubeFace.BACK][2, 2]
    cube.faces[CubeFace.BACK][2, 2] = temp

    assert not cube.is_solvable()


def test_not_solvable_flipped_edge() -> None:
    cube = RubiksCube()

    # Flip single edge
    temp = cube.faces[CubeFace.UP][2, 1]
    cube.faces[CubeFace.UP][2, 1] = cube.faces[CubeFace.FRONT][0, 1]
    cube.faces[CubeFace.FRONT][0, 1] = temp

    assert not cube.is_solvable()


def test_not_solvable_multiple_flipped_edges() -> None:
    cube = RubiksCube()

    # Flip 3 edges
    temp = cube.faces[CubeFace.UP][2, 1]
    cube.faces[CubeFace.UP][2, 1] = cube.faces[CubeFace.FRONT][0, 1]
    cube.faces[CubeFace.FRONT][0, 1] = temp
    temp = cube.faces[CubeFace.DOWN][0, 1]
    cube.faces[CubeFace.DOWN][0, 1] = cube.faces[CubeFace.FRONT][2, 1]
    cube.faces[CubeFace.FRONT][2, 1] = temp
    temp = cube.faces[CubeFace.RIGHT][1, 0]
    cube.faces[CubeFace.RIGHT][1, 0] = cube.faces[CubeFace.FRONT][1, 2]
    cube.faces[CubeFace.FRONT][1, 2] = temp

    assert not cube.is_solvable()
