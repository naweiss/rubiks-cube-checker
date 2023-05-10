import random
from typing import Dict, Tuple

from rubiks_cube_checker.cube import RubiksCube, CubeFace

solved_cube = RubiksCube()


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


def get_edge_parity(edge: Tuple[str, str]) -> int:
    if edge[0] == 'w' or edge[0] == 'y':
        return 0
    if edge[0] == 'g' or edge[0] == 'b':
        if edge[1] == 'r' or edge[1] == 'o':
            return 0
    return 1


def get_corner_parity(corner: Tuple[str, str, str]) -> int:
    if corner[0] == 'w' or corner[0] == 'y':
        return 0
    if corner[1] == 'w' or corner[1] == 'y':
        return 1
    return 2


def total_edge_parity(cube: RubiksCube) -> int:
    return sum([
        get_edge_parity((cube.faces[CubeFace.UP][0, 1], cube.faces[CubeFace.BACK][0, 1])),
        get_edge_parity((cube.faces[CubeFace.UP][1, 2], cube.faces[CubeFace.RIGHT][0, 1])),
        get_edge_parity((cube.faces[CubeFace.UP][2, 1], cube.faces[CubeFace.FRONT][0, 1])),
        get_edge_parity((cube.faces[CubeFace.UP][1, 0], cube.faces[CubeFace.LEFT][0, 1])),
        get_edge_parity((cube.faces[CubeFace.DOWN][0, 1], cube.faces[CubeFace.FRONT][2, 1])),
        get_edge_parity((cube.faces[CubeFace.DOWN][1, 2], cube.faces[CubeFace.RIGHT][2, 1])),
        get_edge_parity((cube.faces[CubeFace.DOWN][2, 1], cube.faces[CubeFace.BACK][2, 1])),
        get_edge_parity((cube.faces[CubeFace.DOWN][1, 0], cube.faces[CubeFace.LEFT][2, 1])),
        get_edge_parity((cube.faces[CubeFace.FRONT][1, 2], cube.faces[CubeFace.RIGHT][1, 0])),
        get_edge_parity((cube.faces[CubeFace.FRONT][1, 0], cube.faces[CubeFace.LEFT][1, 2])),
        get_edge_parity((cube.faces[CubeFace.BACK][1, 2], cube.faces[CubeFace.LEFT][1, 0])),
        get_edge_parity((cube.faces[CubeFace.BACK][1, 0], cube.faces[CubeFace.RIGHT][1, 2])),
    ])


def total_corner_parity(cube: RubiksCube) -> int:
    return sum([
        get_corner_parity(
            (cube.faces[CubeFace.UP][0, 0], cube.faces[CubeFace.BACK][0, 2], cube.faces[CubeFace.LEFT][0, 0])),
        get_corner_parity(
            (cube.faces[CubeFace.UP][0, 2], cube.faces[CubeFace.RIGHT][0, 2], cube.faces[CubeFace.BACK][0, 0])),
        get_corner_parity(
            (cube.faces[CubeFace.UP][2, 0], cube.faces[CubeFace.LEFT][0, 2], cube.faces[CubeFace.FRONT][0, 0])),
        get_corner_parity(
            (cube.faces[CubeFace.UP][2, 2], cube.faces[CubeFace.FRONT][0, 2], cube.faces[CubeFace.RIGHT][0, 0])),
        get_corner_parity(
            (cube.faces[CubeFace.DOWN][0, 0], cube.faces[CubeFace.FRONT][2, 0], cube.faces[CubeFace.LEFT][2, 2])),
        get_corner_parity(
            (cube.faces[CubeFace.DOWN][0, 2], cube.faces[CubeFace.RIGHT][2, 0], cube.faces[CubeFace.FRONT][2, 2])),
        get_corner_parity(
            (cube.faces[CubeFace.DOWN][2, 0], cube.faces[CubeFace.LEFT][2, 0], cube.faces[CubeFace.BACK][2, 2])),
        get_corner_parity(
            (cube.faces[CubeFace.DOWN][2, 2], cube.faces[CubeFace.BACK][2, 0], cube.faces[CubeFace.RIGHT][2, 2])),
    ])


def sort_dict(d: Dict) -> Dict:
    sorted_keys = [tuple(sorted(k)) for k in d.keys()]
    sorted_values = [tuple(sorted(v)) for v in d.values()]
    sorted_dict = dict(zip(sorted_keys, sorted_values))
    return sorted_dict


def calculate_permutation(parings: Dict) -> int:
    parings = sort_dict(parings)
    keys = list(parings.keys())
    start_key = keys.pop()
    key = start_key
    permutations = 0
    while len(keys) > 0:
        value = parings[key]
        if value == start_key:
            start_key = keys.pop()
            key = start_key
        else:
            permutations += 1
            key = value
            keys.remove(key)
    value = parings[key]
    if value != start_key:
        permutations += 1
    return permutations


def total_edge_permutation_parity(cube: RubiksCube) -> int:
    parings = {
        (cube.faces[CubeFace.UP][0, 1], cube.faces[CubeFace.BACK][0, 1]):
            (solved_cube.faces[CubeFace.UP][0, 1], solved_cube.faces[CubeFace.BACK][0, 1]),
        (cube.faces[CubeFace.UP][1, 2], cube.faces[CubeFace.RIGHT][0, 1]):
            (solved_cube.faces[CubeFace.UP][1, 2], solved_cube.faces[CubeFace.RIGHT][0, 1]),
        (cube.faces[CubeFace.UP][2, 1], cube.faces[CubeFace.FRONT][0, 1]):
            (solved_cube.faces[CubeFace.UP][2, 1], solved_cube.faces[CubeFace.FRONT][0, 1]),
        (cube.faces[CubeFace.UP][1, 0], cube.faces[CubeFace.LEFT][0, 1]):
            (solved_cube.faces[CubeFace.UP][1, 0], solved_cube.faces[CubeFace.LEFT][0, 1]),
        (cube.faces[CubeFace.DOWN][0, 1], cube.faces[CubeFace.FRONT][2, 1]):
            (solved_cube.faces[CubeFace.DOWN][0, 1], solved_cube.faces[CubeFace.FRONT][2, 1]),
        (cube.faces[CubeFace.DOWN][1, 2], cube.faces[CubeFace.RIGHT][2, 1]):
            (solved_cube.faces[CubeFace.DOWN][1, 2], solved_cube.faces[CubeFace.RIGHT][2, 1]),
        (cube.faces[CubeFace.DOWN][2, 1], cube.faces[CubeFace.BACK][2, 1]):
            (solved_cube.faces[CubeFace.DOWN][2, 1], solved_cube.faces[CubeFace.BACK][2, 1]),
        (cube.faces[CubeFace.DOWN][1, 0], cube.faces[CubeFace.LEFT][2, 1]):
            (solved_cube.faces[CubeFace.DOWN][1, 0], solved_cube.faces[CubeFace.LEFT][2, 1]),
        (cube.faces[CubeFace.FRONT][1, 2], cube.faces[CubeFace.RIGHT][1, 0]):
            (solved_cube.faces[CubeFace.FRONT][1, 2], solved_cube.faces[CubeFace.RIGHT][1, 0]),
        (cube.faces[CubeFace.FRONT][1, 0], cube.faces[CubeFace.LEFT][1, 2]):
            (solved_cube.faces[CubeFace.FRONT][1, 0], solved_cube.faces[CubeFace.LEFT][1, 2]),
        (cube.faces[CubeFace.BACK][1, 2], cube.faces[CubeFace.LEFT][1, 0]):
            (solved_cube.faces[CubeFace.BACK][1, 2], solved_cube.faces[CubeFace.LEFT][1, 0]),
        (cube.faces[CubeFace.BACK][1, 0], cube.faces[CubeFace.RIGHT][1, 2]):
            (solved_cube.faces[CubeFace.BACK][1, 0], solved_cube.faces[CubeFace.RIGHT][1, 2]),
    }
    return calculate_permutation(parings)


def total_corner_permutation_parity(cube: RubiksCube) -> int:
    parings = {
        (cube.faces[CubeFace.UP][0, 0], cube.faces[CubeFace.BACK][0, 2], cube.faces[CubeFace.LEFT][0, 0]):
            (solved_cube.faces[CubeFace.UP][0, 0], solved_cube.faces[CubeFace.BACK][0, 2],
             solved_cube.faces[CubeFace.LEFT][0, 0]),
        (cube.faces[CubeFace.UP][0, 2], cube.faces[CubeFace.RIGHT][0, 2], cube.faces[CubeFace.BACK][0, 0]):
            (solved_cube.faces[CubeFace.UP][0, 2], solved_cube.faces[CubeFace.RIGHT][0, 2],
             solved_cube.faces[CubeFace.BACK][0, 0]),
        (cube.faces[CubeFace.UP][2, 0], cube.faces[CubeFace.LEFT][0, 2], cube.faces[CubeFace.FRONT][0, 0]):
            (solved_cube.faces[CubeFace.UP][2, 0], solved_cube.faces[CubeFace.LEFT][0, 2],
             solved_cube.faces[CubeFace.FRONT][0, 0]),
        (cube.faces[CubeFace.UP][2, 2], cube.faces[CubeFace.FRONT][0, 2], cube.faces[CubeFace.RIGHT][0, 0]):
            (solved_cube.faces[CubeFace.UP][2, 2], solved_cube.faces[CubeFace.FRONT][0, 2],
             solved_cube.faces[CubeFace.RIGHT][0, 0]),
        (cube.faces[CubeFace.DOWN][0, 0], cube.faces[CubeFace.FRONT][2, 0], cube.faces[CubeFace.LEFT][2, 2]):
            (solved_cube.faces[CubeFace.DOWN][0, 0], solved_cube.faces[CubeFace.FRONT][2, 0],
             solved_cube.faces[CubeFace.LEFT][2, 2]),
        (cube.faces[CubeFace.DOWN][0, 2], cube.faces[CubeFace.RIGHT][2, 0], cube.faces[CubeFace.FRONT][2, 2]):
            (solved_cube.faces[CubeFace.DOWN][0, 2], solved_cube.faces[CubeFace.RIGHT][2, 0],
             solved_cube.faces[CubeFace.FRONT][2, 2]),
        (cube.faces[CubeFace.DOWN][2, 0], cube.faces[CubeFace.LEFT][2, 0], cube.faces[CubeFace.BACK][2, 2]):
            (solved_cube.faces[CubeFace.DOWN][2, 0], solved_cube.faces[CubeFace.LEFT][2, 0],
             solved_cube.faces[CubeFace.BACK][2, 2]),
        (cube.faces[CubeFace.DOWN][2, 2], cube.faces[CubeFace.BACK][2, 0], cube.faces[CubeFace.RIGHT][2, 2]):
            (solved_cube.faces[CubeFace.DOWN][2, 2], solved_cube.faces[CubeFace.BACK][2, 0],
             solved_cube.faces[CubeFace.RIGHT][2, 2]),
    }
    return calculate_permutation(parings)


def assert_is_solvable(cube: RubiksCube) -> None:
    assert (total_edge_parity(cube) % 2 == 0 and
            total_corner_parity(cube) % 3 == 0 and
            total_edge_permutation_parity(cube) % 2 == total_corner_permutation_parity(cube) % 2)


def test_solvable():
    # TODO: move to rubiks_cube_checker
    cube = RubiksCube()
    # rotate_edges(cube)
    # rotate_corners(cube)
    print('\n{}'.format(cube))
    for _ in range(100):
        for move in random.choice(["U", "D", "R", "L", "F", "B"]):
            cube.do_move(move)
        assert_is_solvable(cube)
