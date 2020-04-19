def get_ints():
    return map(int, input().split())

import numpy as np


def geom(r, n):
    # r + r*2 + ... + r**(n-1)
    if r == 1:
        return n - 1
    return (1 - r**n) // (1 - r) - 1


mod = 1000000007


def gen_stair(N, K):
    current_step = 0
    stair = np.ndarray(N, dtype=np.int64)
    for i in range(N):
        current_step += geom(i + 1, K + 1)
        current_step %= mod
        stair[i] = current_step
    return stair


def main(case_id):
    N, K, x, y, C, D, Ex, Ey, F = get_ints()
    # Generate array
    A = np.ndarray(N, dtype=np.int64)
    for i in range(N):
        A[i] = (x + y) % F
        x, y = (C * x + D * y + Ex) % F, (C * y + D * x + Ey) % F

    # # naive implementation
    # result = 0
    # for k in range(1, K+1):
    #     for L in range(N):
    #         for R in range(L, N):
    #             for j in range(L, R+1):
    #                 result = result + pow(j-L+1, k) * int(A[j])
    #                 result %= 1000000007

    a987654321 = np.arange(N, 0, -1, dtype=np.int64)
    stair = gen_stair(N, K)
    result = A * stair % mod
    result = result * a987654321 % mod
    result = np.sum(result) % mod

    print("Case #{}: {}".format(case_id, result))
    # print("Powers:", powers)
    # print(f"Case #{case_id}: {max_beauty} <{L} {M} {H}>")


(T, ) = get_ints()
for i in range(T):
    main(i + 1)
