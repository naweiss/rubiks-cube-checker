from typing import Dict, Sequence, Tuple


def _sort_dict(d: Dict) -> Dict:
    sorted_keys = [tuple(sorted(k)) for k in d]
    sorted_values = [tuple(sorted(v)) for v in d.values()]
    return dict(zip(sorted_keys, sorted_values))


def permutation_parity(current_state: Sequence[Tuple[str, ...]], solved_state: Sequence[Tuple[str, ...]]) -> int:
    parings = dict(zip(current_state, solved_state))

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
