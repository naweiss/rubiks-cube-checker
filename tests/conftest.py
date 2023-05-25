from typing import Dict, List

import numpy as np
import pytest
from _pytest.fixtures import SubRequest

from rubiks_cube_checker.cube import CubeFace


@pytest.fixture(params=['U', 'D', 'R', 'L', 'F', 'B'])
def move(request: SubRequest) -> str:
    return request.param  # type: ignore[no-any-return]


@pytest.fixture(scope='session')
def scrambled_cube_state() -> Dict[str, np.ndarray]:
    """ A random cube scramble """
    return {
        CubeFace.UP: np.array([
            ['o', 'r', 'y'],
            ['g', 'w', 'g'],
            ['o', 'y', 'g']
        ]),
        CubeFace.DOWN: np.array([
            ['o', 'w', 'w'],
            ['o', 'y', 'y'],
            ['b', 'b', 'y']
        ]),
        CubeFace.FRONT: np.array([
            ['b', 'r', 'y'],
            ['w', 'g', 'y'],
            ['y', 'g', 'r']
        ]),
        CubeFace.BACK: np.array([
            ['b', 'g', 'g'],
            ['b', 'b', 'w'],
            ['b', 'w', 'r']
        ]),
        CubeFace.LEFT: np.array([
            ['w', 'o', 'w'],
            ['o', 'o', 'r'],
            ['w', 'b', 'g']
        ]),
        CubeFace.RIGHT: np.array([
            ['r', 'y', 'o'],
            ['b', 'r', 'r'],
            ['g', 'o', 'r']
        ])
    }


@pytest.fixture(scope='session')
def cube_scramble_moves() -> List[str]:
    """ The moves needed to reach the scrambled_cube_state starting with a solved cube """
    return [
        "B'", "R2", "F'", "B", "U'", "F", "L2",
        "R2", "B2", "U", "L", "D'", "F2", "D2",
        "L", "R", "F'", "L2", "D2", "L'", "R2",
        "B2", "D'", "U'", "L'"
    ]


@pytest.fixture(scope='session')
def scrambled_cube_state_after_u_move() -> Dict[str, np.ndarray]:
    """ The cube state after a U move starting with scrambled_cube_state """
    return {
        CubeFace.UP: np.array([
            ['o', 'g', 'o'],
            ['y', 'w', 'r'],
            ['g', 'g', 'y']
        ]),
        CubeFace.DOWN: np.array([
            ['o', 'w', 'w'],
            ['o', 'y', 'y'],
            ['b', 'b', 'y']
        ]),
        CubeFace.FRONT: np.array([
            ['r', 'y', 'o'],
            ['w', 'g', 'y'],
            ['y', 'g', 'r']
        ]),
        CubeFace.BACK: np.array([
            ['w', 'o', 'w'],
            ['b', 'b', 'w'],
            ['b', 'w', 'r']
        ]),
        CubeFace.LEFT: np.array([
            ['b', 'r', 'y'],
            ['o', 'o', 'r'],
            ['w', 'b', 'g']
        ]),
        CubeFace.RIGHT: np.array([
            ['b', 'g', 'g'],
            ['b', 'r', 'r'],
            ['g', 'o', 'r']
        ])
    }


@pytest.fixture(scope='session')
def scrambled_cube_state_after_d_move() -> Dict[str, np.ndarray]:
    """ The cube state after a D move starting with scrambled_cube_state """
    return {
        CubeFace.UP: np.array([
            ['o', 'r', 'y'],
            ['g', 'w', 'g'],
            ['o', 'y', 'g']
        ]),
        CubeFace.DOWN: np.array([
            ['b', 'o', 'o'],
            ['b', 'y', 'w'],
            ['y', 'y', 'w']
        ]),
        CubeFace.FRONT: np.array([
            ['b', 'r', 'y'],
            ['w', 'g', 'y'],
            ['w', 'b', 'g']
        ]),
        CubeFace.BACK: np.array([
            ['b', 'g', 'g'],
            ['b', 'b', 'w'],
            ['g', 'o', 'r']
        ]),
        CubeFace.LEFT: np.array([
            ['w', 'o', 'w'],
            ['o', 'o', 'r'],
            ['b', 'w', 'r']
        ]),
        CubeFace.RIGHT: np.array([
            ['r', 'y', 'o'],
            ['b', 'r', 'r'],
            ['y', 'g', 'r']
        ])
    }


@pytest.fixture(scope='session')
def scrambled_cube_state_after_f_move() -> Dict[str, np.ndarray]:
    """ The cube state after an F move starting with scrambled_cube_state """
    return {
        CubeFace.UP: np.array([
            ['o', 'r', 'y'],
            ['g', 'w', 'g'],
            ['g', 'r', 'w'],
        ]),
        CubeFace.DOWN: np.array([
            ['g', 'b', 'r'],
            ['o', 'y', 'y'],
            ['b', 'b', 'y']
        ]),
        CubeFace.FRONT: np.array([
            ['y', 'w', 'b'],
            ['g', 'g', 'r'],
            ['r', 'y', 'y']
        ]),
        CubeFace.BACK: np.array([
            ['b', 'g', 'g'],
            ['b', 'b', 'w'],
            ['b', 'w', 'r']
        ]),
        CubeFace.LEFT: np.array([
            ['w', 'o', 'o'],
            ['o', 'o', 'w'],
            ['w', 'b', 'w']
        ]),
        CubeFace.RIGHT: np.array([
            ['o', 'y', 'o'],
            ['y', 'r', 'r'],
            ['g', 'o', 'r']
        ])
    }


@pytest.fixture(scope='session')
def scrambled_cube_state_after_b_move() -> Dict[str, np.ndarray]:
    """ The cube state after a B move starting with scrambled_cube_state """
    return {
        CubeFace.UP: np.array([
            ['o', 'r', 'r'],
            ['g', 'w', 'g'],
            ['o', 'y', 'g']
        ]),
        CubeFace.DOWN: np.array([
            ['o', 'w', 'w'],
            ['o', 'y', 'y'],
            ['w', 'o', 'w']
        ]),
        CubeFace.FRONT: np.array([
            ['b', 'r', 'y'],
            ['w', 'g', 'y'],
            ['y', 'g', 'r']
        ]),
        CubeFace.BACK: np.array([
            ['b', 'b', 'b'],
            ['w', 'b', 'g'],
            ['r', 'w', 'g']
        ]),
        CubeFace.LEFT: np.array([
            ['y', 'o', 'w'],
            ['r', 'o', 'r'],
            ['o', 'b', 'g']
        ]),
        CubeFace.RIGHT: np.array([
            ['r', 'y', 'y'],
            ['b', 'r', 'b'],
            ['g', 'o', 'b']
        ])
    }


@pytest.fixture(scope='session')
def scrambled_cube_state_after_r_move() -> Dict[str, np.ndarray]:
    """ The cube state after an R move starting with scrambled_cube_state """
    return {
        CubeFace.UP: np.array([
            ['o', 'r', 'y'],
            ['g', 'w', 'y'],
            ['o', 'y', 'r']
        ]),
        CubeFace.DOWN: np.array([
            ['o', 'w', 'b'],
            ['o', 'y', 'b'],
            ['b', 'b', 'b']
        ]),
        CubeFace.FRONT: np.array([
            ['b', 'r', 'w'],
            ['w', 'g', 'y'],
            ['y', 'g', 'y']
        ]),
        CubeFace.BACK: np.array([
            ['g', 'g', 'g'],
            ['g', 'b', 'w'],
            ['y', 'w', 'r']
        ]),
        CubeFace.LEFT: np.array([
            ['w', 'o', 'w'],
            ['o', 'o', 'r'],
            ['w', 'b', 'g']
        ]),
        CubeFace.RIGHT: np.array([
            ['g', 'b', 'r'],
            ['o', 'r', 'y'],
            ['r', 'r', 'o']
        ])
    }


@pytest.fixture(scope='session')
def scrambled_cube_state_after_l_move() -> Dict[str, np.ndarray]:
    """ The cube state after an L move starting with scrambled_cube_state """
    return {
        CubeFace.UP: np.array([
            ['r', 'r', 'y'],
            ['w', 'w', 'g'],
            ['g', 'y', 'g']
        ]),
        CubeFace.DOWN: np.array([
            ['b', 'w', 'w'],
            ['w', 'y', 'y'],
            ['y', 'b', 'y']
        ]),
        CubeFace.FRONT: np.array([
            ['o', 'r', 'y'],
            ['g', 'g', 'y'],
            ['o', 'g', 'r']
        ]),
        CubeFace.BACK: np.array([
            ['b', 'g', 'b'],
            ['b', 'b', 'o'],
            ['b', 'w', 'o']
        ]),
        CubeFace.LEFT: np.array([
            ['w', 'o', 'w'],
            ['b', 'o', 'o'],
            ['g', 'r', 'w']
        ]),
        CubeFace.RIGHT: np.array([
            ['r', 'y', 'o'],
            ['b', 'r', 'r'],
            ['g', 'o', 'r']
        ])
    }
