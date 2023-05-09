import numpy as np
import pytest


@pytest.fixture(params=["U", "D", "R", "L", "F", "B"])
def move(request):
    return request.param


@pytest.fixture
def scrambled_cube_state():
    """ A random cube scramble """
    return {
        "U": np.array([
            ["o", "r", "y"],
            ["g", "w", "g"],
            ["o", "y", "g"]
        ]),
        "D": np.array([
            ["o", "w", "w"],
            ["o", "y", "y"],
            ["b", "b", "y"]
        ]),
        "F": np.array([
            ["b", "r", "y"],
            ["w", "g", "y"],
            ["y", "g", "r"]
        ]),
        "B": np.array([
            ["b", "g", "g"],
            ["b", "b", "w"],
            ["b", "w", "r"]
        ]),
        "L": np.array([
            ["w", "o", "w"],
            ["o", "o", "r"],
            ["w", "b", "g"]
        ]),
        "R": np.array([
            ["r", "y", "o"],
            ["b", "r", "r"],
            ["g", "o", "r"]
        ])
    }


@pytest.fixture(scope='session')
def cube_scramble_moves():
    """ The moves needed to reach the scrambled_cube_state starting with a solved cube """
    return [
        "B'", "R2", "F'", "B", "U'", "F", "L2",
        "R2", "B2", "U", "L", "D'", "F2", "D2",
        "L", "R", "F'", "L2", "D2", "L'", "R2",
        "B2", "D'", "U'", "L'"
    ]
