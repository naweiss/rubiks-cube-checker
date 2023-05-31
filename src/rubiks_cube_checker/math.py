from typing import FrozenSet, Iterator, Sequence, Tuple


def _to_frozen_sets(tuples: Sequence[Tuple]) -> Iterator[FrozenSet]:
    return (frozenset(_tuple) for _tuple in tuples)


def permutation_parity(permutation: Sequence[Tuple], natural_order: Sequence[Tuple]) -> int:
    """
    Calculate the parity of the permutation of a sequence given its natural order.
    e.g. does the number of swapped elements in the sequence (based on the natural order) is even or odd.

    :param permutation: Some ordering of elements
    :type permutation: Sequence of tuples (elements), each tuple represent a set (the order does not matter)
    :param natural_order: The natural order of the elements
    :type permutation: Sequence of tuples (elements), each tuple represent a set (the order does not matter)
    :return: 1 if the permutation is odd and 0 if it is even
    """
    keys = list(_to_frozen_sets(permutation))

    state_mappings = dict(zip(keys, _to_frozen_sets(natural_order)))
    permutations = 0
    while len(keys) > 0:
        start_key = keys.pop()
        key = start_key
        while True:
            key = state_mappings[key]
            if key == start_key:
                break
            permutations += 1
            keys.remove(key)
    return permutations % 2
