from typing import Dict

import numpy as np

from rubiks_cube_checker.cube import RubiksCube, CubeFace


def test_default_cube() -> None:
    cube = RubiksCube()
    assert np.array_equal(cube.faces[CubeFace.UP], np.full(shape=(3, 3), fill_value='w'))
    assert np.array_equal(cube.faces[CubeFace.DOWN], np.full(shape=(3, 3), fill_value='y'))
    assert np.array_equal(cube.faces[CubeFace.LEFT], np.full(shape=(3, 3), fill_value='o'))
    assert np.array_equal(cube.faces[CubeFace.RIGHT], np.full(shape=(3, 3), fill_value='r'))
    assert np.array_equal(cube.faces[CubeFace.FRONT], np.full(shape=(3, 3), fill_value='g'))
    assert np.array_equal(cube.faces[CubeFace.BACK], np.full(shape=(3, 3), fill_value='b'))


def test_initialization(scrambled_cube_state: Dict[str, np.ndarray]) -> None:
    cube = RubiksCube(faces=scrambled_cube_state)
    assert np.array_equal(cube.faces[CubeFace.UP], scrambled_cube_state[CubeFace.UP])
    assert np.array_equal(cube.faces[CubeFace.DOWN], scrambled_cube_state[CubeFace.DOWN])
    assert np.array_equal(cube.faces[CubeFace.LEFT], scrambled_cube_state[CubeFace.LEFT])
    assert np.array_equal(cube.faces[CubeFace.RIGHT], scrambled_cube_state[CubeFace.RIGHT])
    assert np.array_equal(cube.faces[CubeFace.FRONT], scrambled_cube_state[CubeFace.FRONT])
    assert np.array_equal(cube.faces[CubeFace.BACK], scrambled_cube_state[CubeFace.BACK])
