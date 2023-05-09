from rubiks_cube_checker.cube import RubiksCube


def test_do_move_simple_notation(scrambled_cube_state, move):
    cube_a = RubiksCube(faces=scrambled_cube_state)
    cube_b = RubiksCube(faces=scrambled_cube_state)

    cube_a.do_move(move)
    cube_b.rotate(move)

    assert cube_b == cube_a


def test_do_move_double_notation(scrambled_cube_state, move):
    cube_a = RubiksCube(faces=scrambled_cube_state)
    cube_b = RubiksCube(faces=scrambled_cube_state)

    cube_a.do_move(f"{move}2")
    for _ in range(2):
        cube_b.rotate(move)

    assert cube_b == cube_a


def test_do_move_inverse_notation(scrambled_cube_state, move):
    cube_a = RubiksCube(faces=scrambled_cube_state)
    cube_b = RubiksCube(faces=scrambled_cube_state)

    cube_a.do_move(f"{move}'")
    for _ in range(3):
        cube_b.rotate(move)

    assert cube_b == cube_a


def test_do_move_multiple(cube_scramble_moves, scrambled_cube_state):
    cube = RubiksCube()
    for move in cube_scramble_moves:
        cube.do_move(move)

    assert cube == RubiksCube(faces=scrambled_cube_state)
