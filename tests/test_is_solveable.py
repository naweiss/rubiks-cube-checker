import random

from rubiks_cube_checker.cube import RubiksCube


# TODO: delete
def rotate_edges(cube):
    temp = cube.faces['U'][2, 1]
    cube.faces['U'][2, 1] = cube.faces['F'][0, 1]
    cube.faces['F'][0, 1] = temp
    temp = cube.faces['D'][0, 1]
    cube.faces['D'][0, 1] = cube.faces['F'][2, 1]
    cube.faces['F'][2, 1] = temp
    temp = cube.faces['R'][1, 0]
    cube.faces['R'][1, 0] = cube.faces['F'][1, 2]
    cube.faces['F'][1, 2] = temp
    temp = cube.faces['L'][1, 2]
    cube.faces['L'][1, 2] = cube.faces['F'][1, 0]
    cube.faces['F'][1, 0] = temp


def get_edge_parity(edge):
    if edge[0] == 'w' or edge[0] == 'y':
        return 0
    if edge[0] == 'g' or edge[0] == 'b':
        if edge[1] == 'r' or edge[1] == 'o':
            return 0
    return 1


def get_corner_parity(corner):
    if corner[0] == 'w' or corner[0] == 'y':
        return 0
    if corner[1] == 'w' or corner[1] == 'y':
        return 1
    return 2


def total_edge_parity(cube):
    return sum([
        get_edge_parity([cube.faces['U'][0, 1], cube.faces['B'][0, 1]]),
        get_edge_parity([cube.faces['U'][1, 2], cube.faces['R'][0, 1]]),
        get_edge_parity([cube.faces['U'][2, 1], cube.faces['F'][0, 1]]),
        get_edge_parity([cube.faces['U'][1, 0], cube.faces['L'][0, 1]]),
        get_edge_parity([cube.faces['D'][0, 1], cube.faces['F'][2, 1]]),
        get_edge_parity([cube.faces['D'][1, 2], cube.faces['R'][2, 1]]),
        get_edge_parity([cube.faces['D'][2, 1], cube.faces['B'][2, 1]]),
        get_edge_parity([cube.faces['D'][1, 0], cube.faces['L'][2, 1]]),
        get_edge_parity([cube.faces['F'][1, 2], cube.faces['R'][1, 0]]),
        get_edge_parity([cube.faces['F'][1, 0], cube.faces['L'][1, 2]]),
        get_edge_parity([cube.faces['B'][1, 2], cube.faces['L'][1, 0]]),
        get_edge_parity([cube.faces['B'][1, 0], cube.faces['R'][1, 2]]),
    ])


def total_corner_parity(cube):
    return sum([
        get_corner_parity([cube.faces['U'][0, 0], cube.faces['B'][0, 2], cube.faces['L'][0, 0]]),
        get_corner_parity([cube.faces['U'][0, 2], cube.faces['R'][0, 2], cube.faces['B'][0, 0]]),
        get_corner_parity([cube.faces['U'][2, 0], cube.faces['L'][0, 2], cube.faces['F'][0, 0]]),
        get_corner_parity([cube.faces['U'][2, 2], cube.faces['F'][0, 2], cube.faces['R'][0, 0]]),
        get_corner_parity([cube.faces['D'][0, 0], cube.faces['F'][2, 0], cube.faces['L'][2, 2]]),
        get_corner_parity([cube.faces['D'][0, 2], cube.faces['R'][2, 0], cube.faces['F'][2, 2]]),
        get_corner_parity([cube.faces['D'][2, 0], cube.faces['L'][2, 0], cube.faces['B'][2, 2]]),
        get_corner_parity([cube.faces['D'][2, 2], cube.faces['B'][2, 0], cube.faces['R'][2, 2]]),
    ])


def sort_dict(d):
    sorted_keys = [tuple(sorted(k)) for k in d.keys()]
    sorted_values = [tuple(sorted(v)) for v in d.values()]
    sorted_dict = dict(zip(sorted_keys, sorted_values))
    return sorted_dict


def calculate_permutation(parings):
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


def total_edge_permutation_parity(cube):
    solved_cube = RubiksCube()
    parings = {
        (cube.faces['U'][0, 1], cube.faces['B'][0, 1]):
            (solved_cube.faces['U'][0, 1], solved_cube.faces['B'][0, 1]),
        (cube.faces['U'][1, 2], cube.faces['R'][0, 1]):
            (solved_cube.faces['U'][1, 2], solved_cube.faces['R'][0, 1]),
        (cube.faces['U'][2, 1], cube.faces['F'][0, 1]):
            (solved_cube.faces['U'][2, 1], solved_cube.faces['F'][0, 1]),
        (cube.faces['U'][1, 0], cube.faces['L'][0, 1]):
            (solved_cube.faces['U'][1, 0], solved_cube.faces['L'][0, 1]),
        (cube.faces['D'][0, 1], cube.faces['F'][2, 1]):
            (solved_cube.faces['D'][0, 1], solved_cube.faces['F'][2, 1]),
        (cube.faces['D'][1, 2], cube.faces['R'][2, 1]):
            (solved_cube.faces['D'][1, 2], solved_cube.faces['R'][2, 1]),
        (cube.faces['D'][2, 1], cube.faces['B'][2, 1]):
            (solved_cube.faces['D'][2, 1], solved_cube.faces['B'][2, 1]),
        (cube.faces['D'][1, 0], cube.faces['L'][2, 1]):
            (solved_cube.faces['D'][1, 0], solved_cube.faces['L'][2, 1]),
        (cube.faces['F'][1, 2], cube.faces['R'][1, 0]):
            (solved_cube.faces['F'][1, 2], solved_cube.faces['R'][1, 0]),
        (cube.faces['F'][1, 0], cube.faces['L'][1, 2]):
            (solved_cube.faces['F'][1, 0], solved_cube.faces['L'][1, 2]),
        (cube.faces['B'][1, 2], cube.faces['L'][1, 0]):
            (solved_cube.faces['B'][1, 2], solved_cube.faces['L'][1, 0]),
        (cube.faces['B'][1, 0], cube.faces['R'][1, 2]):
            (solved_cube.faces['B'][1, 0], solved_cube.faces['R'][1, 2]),
    }
    return calculate_permutation(parings)


def total_corner_permutation_parity(cube):
    solved_cube = RubiksCube()
    parings = {
        (cube.faces['U'][0, 0], cube.faces['B'][0, 2], cube.faces['L'][0, 0]):
            (solved_cube.faces['U'][0, 0], solved_cube.faces['B'][0, 2], solved_cube.faces['L'][0, 0]),
        (cube.faces['U'][0, 2], cube.faces['R'][0, 2], cube.faces['B'][0, 0]):
            (solved_cube.faces['U'][0, 2], solved_cube.faces['R'][0, 2], solved_cube.faces['B'][0, 0]),
        (cube.faces['U'][2, 0], cube.faces['L'][0, 2], cube.faces['F'][0, 0]):
            (solved_cube.faces['U'][2, 0], solved_cube.faces['L'][0, 2], solved_cube.faces['F'][0, 0]),
        (cube.faces['U'][2, 2], cube.faces['F'][0, 2], cube.faces['R'][0, 0]):
            (solved_cube.faces['U'][2, 2], solved_cube.faces['F'][0, 2], solved_cube.faces['R'][0, 0]),
        (cube.faces['D'][0, 0], cube.faces['F'][2, 0], cube.faces['L'][2, 2]):
            (solved_cube.faces['D'][0, 0], solved_cube.faces['F'][2, 0], solved_cube.faces['L'][2, 2]),
        (cube.faces['D'][0, 2], cube.faces['R'][2, 0], cube.faces['F'][2, 2]):
            (solved_cube.faces['D'][0, 2], solved_cube.faces['R'][2, 0], solved_cube.faces['F'][2, 2]),
        (cube.faces['D'][2, 0], cube.faces['L'][2, 0], cube.faces['B'][2, 2]):
            (solved_cube.faces['D'][2, 0], solved_cube.faces['L'][2, 0], solved_cube.faces['B'][2, 2]),
        (cube.faces['D'][2, 2], cube.faces['B'][2, 0], cube.faces['R'][2, 2]):
            (solved_cube.faces['D'][2, 2], solved_cube.faces['B'][2, 0], solved_cube.faces['R'][2, 2]),
    }
    return calculate_permutation(parings)


def test_solvable():
    # TODO: move to rubiks_cube_checker
    def assert_is_solvable(cube):
        assert (total_edge_parity(cube) % 2 == 0 and
                total_corner_parity(cube) % 3 == 0 and
                total_edge_permutation_parity(cube) % 2 == total_corner_permutation_parity(cube) % 2)

    cube = RubiksCube()
    # rotate_edges(cube)
    # rotate_corners(cube)
    print('\n{}'.format(cube))
    for _ in range(100):
        for move in random.choice(["U", "D", "R", "L", "F", "B"]):
            cube.do_move(move)
        assert_is_solvable(cube)
