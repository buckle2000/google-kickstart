def get_ints():
    return tuple(map(int, input().split()))


import numpy as np


def calc_time(skills):
    return np.sum(skills[-1] - skills)

import math

def main(N, P, skills):
    skills = np.sort(skills)
    best_time = math.inf
    time = None
    for i in range(N - P + 1):
        if time is None:
            time = int(calc_time(skills[i:P+i]))
        else:
            time -= skills[P+i-1] - skills[i-1]
            time += (skills[P+i-1] - skills[P+i-2]) * P
        # print(time)
        best_time = min(best_time, time)
    return best_time


T, = get_ints()
for i in range(T):
    N, P = get_ints()
    skills = np.array(get_ints())
    ans = main(N, P, skills)
    print("Case #{}: {}".format(i+1, ans))