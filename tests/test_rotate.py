from __future__ import annotations

from typing import TYPE_CHECKING, Dict

from rubiks_cube_checker.cube import RubiksCube

if TYPE_CHECKING:
    from numpy.typing import NDArray


def test_u_rotate(scrambled_cube_state: Dict[str, NDArray],
                  scrambled_cube_state_after_u_move: Dict[str, NDArray]) -> None:
    cube = RubiksCube(faces=scrambled_cube_state)
    cube.rotate('U')

    rotated_cube = RubiksCube(faces=scrambled_cube_state_after_u_move)

    assert cube == rotated_cube


def test_d_rotate(scrambled_cube_state: Dict[str, NDArray],
                  scrambled_cube_state_after_d_move: Dict[str, NDArray]) -> None:
    cube = RubiksCube(faces=scrambled_cube_state)
    cube.rotate('D')

    rotated_cube = RubiksCube(faces=scrambled_cube_state_after_d_move)

    assert cube == rotated_cube


def test_f_rotate(scrambled_cube_state: Dict[str, NDArray],
                  scrambled_cube_state_after_f_move: Dict[str, NDArray]) -> None:
    cube = RubiksCube(faces=scrambled_cube_state)
    cube.rotate('F')

    rotated_cube = RubiksCube(faces=scrambled_cube_state_after_f_move)

    assert cube == rotated_cube


def test_b_rotate(scrambled_cube_state: Dict[str, NDArray],
                  scrambled_cube_state_after_b_move: Dict[str, NDArray]) -> None:
    cube = RubiksCube(faces=scrambled_cube_state)
    cube.rotate('B')

    rotated_cube = RubiksCube(faces=scrambled_cube_state_after_b_move)

    assert cube == rotated_cube


def test_r_rotate(scrambled_cube_state: Dict[str, NDArray],
                  scrambled_cube_state_after_r_move: Dict[str, NDArray]) -> None:
    cube = RubiksCube(faces=scrambled_cube_state)
    cube.rotate('R')

    rotated_cube = RubiksCube(faces=scrambled_cube_state_after_r_move)

    assert cube == rotated_cube


def test_l_rotate(scrambled_cube_state: Dict[str, NDArray],
                  scrambled_cube_state_after_l_move: Dict[str, NDArray]) -> None:
    cube = RubiksCube(faces=scrambled_cube_state)
    cube.rotate('L')

    rotated_cube = RubiksCube(faces=scrambled_cube_state_after_l_move)

    assert cube == rotated_cube
