from rubiks_cube_checker.cube import RubiksCube


def test_rotate(scrambled_cube_state, move):
    cube = RubiksCube(faces=scrambled_cube_state)
    # TODO: fill in
