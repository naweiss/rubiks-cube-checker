from typing import Dict, Tuple, Sequence


def _sort_dict(d: Dict) -> Dict:
    sorted_keys = [tuple(sorted(k)) for k in d.keys()]
    sorted_values = [tuple(sorted(v)) for v in d.values()]
    sorted_dict = dict(zip(sorted_keys, sorted_values))
    return sorted_dict


def permutation_parity(current_state: Sequence[Tuple[str, ...]], solved_state: Sequence[Tuple[str, ...]]) -> int:
    parings = {
        element: solved_element
        for element, solved_element in zip(current_state, solved_state)
    }

    parings = _sort_dict(parings)
    keys = list(parings.keys())
    permutations = 0
    while len(keys) > 0:
        start_key = keys.pop()
        key = start_key
        while True:
            key = parings[key]
            if key == start_key:
                break
            permutations += 1
            keys.remove(key)
    return permutations % 2
