from itertools import permutations


def possible_permutations(sequence: list):
    for el in permutations(sequence):
        yield list(el)
        