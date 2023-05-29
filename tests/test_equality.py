from __future__ import annotations

from typing import TYPE_CHECKING, Dict

from rubiks_cube_checker.cube import RubiksCube

if TYPE_CHECKING:
    from numpy.typing import NDArray


def test_equality_sanity(scrambled_cube_state: Dict[str, NDArray]) -> None:
    cube_a = RubiksCube(faces=scrambled_cube_state)
    cube_b = RubiksCube(faces=scrambled_cube_state)
    assert cube_a == cube_b


def test_inequality_sanity(scrambled_cube_state: Dict[str, NDArray]) -> None:
    solved_cube = RubiksCube()
    scrambled_cube = RubiksCube(faces=scrambled_cube_state)
    assert solved_cube != scrambled_cube


def test_inequality(scrambled_cube_state: Dict[str, NDArray], move: str) -> None:
    cube_a = RubiksCube(faces=scrambled_cube_state)
    cube_b = RubiksCube(faces=scrambled_cube_state)
    cube_b.rotate(move)
    assert cube_a != cube_b


def test_equality(scrambled_cube_state: Dict[str, NDArray], move: str) -> None:
    cube_a = RubiksCube(faces=scrambled_cube_state)
    cube_a.rotate(move)

    cube_b = RubiksCube(faces=scrambled_cube_state)
    cube_b.rotate(move)

    assert cube_a == cube_b
