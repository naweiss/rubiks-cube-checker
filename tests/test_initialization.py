import numpy as np

from rubiks_cube_checker.cube import RubiksCube


def test_default_cube():
    cube = RubiksCube()
    assert np.array_equal(cube.faces['U'], np.full(shape=(3, 3), fill_value='w'))
    assert np.array_equal(cube.faces['D'], np.full(shape=(3, 3), fill_value='y'))
    assert np.array_equal(cube.faces['L'], np.full(shape=(3, 3), fill_value='o'))
    assert np.array_equal(cube.faces['R'], np.full(shape=(3, 3), fill_value='r'))
    assert np.array_equal(cube.faces['F'], np.full(shape=(3, 3), fill_value='g'))
    assert np.array_equal(cube.faces['B'], np.full(shape=(3, 3), fill_value='b'))


def test_initialization(scrambled_cube_state):
    cube = RubiksCube(faces=scrambled_cube_state)
    assert np.array_equal(cube.faces['U'], scrambled_cube_state['U'])
    assert np.array_equal(cube.faces['D'], scrambled_cube_state['D'])
    assert np.array_equal(cube.faces['L'], scrambled_cube_state['L'])
    assert np.array_equal(cube.faces['R'], scrambled_cube_state['R'])
    assert np.array_equal(cube.faces['F'], scrambled_cube_state['F'])
    assert np.array_equal(cube.faces['B'], scrambled_cube_state['B'])
