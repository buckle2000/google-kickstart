#!/usr/bin/env python

"""Genreate example"""

import random


def calc_beauty(wall, L, H):
    """Naive"""
    return sum(wall[L : H + 1])


def main_calc_max_beauty(wall):
    """ Correct but naive solution """
    wall = list(map(int, wall))
    N = len(wall)
    max_beauty = 0
    for L in range(0, N):
        for H in range(L, N - N // 2 + L):
            # (H - L) * 2 < N
            # H < N/2 + L
            # H < N-N//2 + L
            beauty = calc_beauty(wall, L, H)
            max_beauty = max(beauty, max_beauty)
    return max_beauty


N = 10 ** 3
with open("in2", "w") as fin:
    print(1, file=fin)
    print(N, file=fin)
    wall = ""
    for _ in range(N):
        wall += random.choice("1234567890")
    print(wall, file=fin)

with open("out2", "w") as fout:
    print("Case #1:", main_calc_max_beauty(wall), file=fout)
