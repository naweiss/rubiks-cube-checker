import random

from rubiks_cube_checker.cube import RubiksCube, CubeFace


# TODO: delete
def rotate_edges(cube: RubiksCube) -> None:
    temp = cube.faces[CubeFace.UP][2, 1]
    cube.faces[CubeFace.UP][2, 1] = cube.faces[CubeFace.FRONT][0, 1]
    cube.faces[CubeFace.FRONT][0, 1] = temp
    temp = cube.faces[CubeFace.DOWN][0, 1]
    cube.faces[CubeFace.DOWN][0, 1] = cube.faces[CubeFace.FRONT][2, 1]
    cube.faces[CubeFace.FRONT][2, 1] = temp
    temp = cube.faces[CubeFace.RIGHT][1, 0]
    cube.faces[CubeFace.RIGHT][1, 0] = cube.faces[CubeFace.FRONT][1, 2]
    cube.faces[CubeFace.FRONT][1, 2] = temp
    temp = cube.faces[CubeFace.LEFT][1, 2]
    cube.faces[CubeFace.LEFT][1, 2] = cube.faces[CubeFace.FRONT][1, 0]
    cube.faces[CubeFace.FRONT][1, 0] = temp


def test_solvable():
    cube = RubiksCube()
    # rotate_edges(cube)
    # rotate_corners(cube)
    for _ in range(100):
        for move in random.choice(["U", "D", "R", "L", "F", "B"]):
            cube.do_move(move)
        assert(cube.is_solvable())
