from typing import Dict, List, Tuple


def _sort_dict(d: Dict) -> Dict:
    sorted_keys = [tuple(sorted(k)) for k in d.keys()]
    sorted_values = [tuple(sorted(v)) for v in d.values()]
    sorted_dict = dict(zip(sorted_keys, sorted_values))
    return sorted_dict


def permutation_parity(current_state: List[Tuple[str, ...]], solved_state: List[Tuple[str, ...]]) -> int:
    parings = {
        element: solved_element
        for element, solved_element in zip(current_state, solved_state)
    }
    parings = _sort_dict(parings)
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
    return permutations % 2
