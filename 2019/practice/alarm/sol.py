def get_ints():
    return map(int, input().split())


def calc_power(A, N, pow_cache):
    """Naive"""

    def _gen_subarray_power():
        for L in range(0, N):  # inclusive
            last_power = None
            for H in range(L + 1, N + 1):  # exclusive
                if last_power is None:
                    power = sum(A[p] * pow_cache[p - L] for p in range(L, H))
                else:
                    p = H - 1
                    power = last_power + A[p] * pow_cache[p - L]
                power = power
                last_power = power
                # print(L, H, i, power)
                yield power % 1000000007

    return sum(_gen_subarray_power())

import numpy as np

def main(case_id):
    N, K, x, y, C, D, Ex, Ey, F = get_ints()
    x, y, A = [x], [y], [(x + y) % F]
    for _ in range(N - 1):
        x_next = (C * x[-1] + D * y[-1] + Ex) % F
        y_next = (C * y[-1] + D * x[-1] + Ey) % F
        x.append(x_next)
        y.append(y_next)
        A.append((x_next + y_next) % F)
    assert len(A) == N

    # N: length of A
    # K: 1...Kth power to sum up
    # A: array
    # pow_cache = None
    def gen_powers():
        pow_cache = np.full(N, 1) # pow cache for i; j**i == pow_cache[j+1]
        stair = np.arange(N, dtype=int) + 1
        for _i in range(1, K + 1):
            # pow_cache = [(j + 1) ** i for j in range(N)]
            pow_cache *= stair
            pow_cache %= 1000000007
            yield calc_power(A, N, pow_cache) % 1000000007

    power = sum(gen_powers()) % 1000000007
    print("Case #{}: {}".format(case_id, power))
    # print("Powers:", powers)
    # print(f"Case #{case_id}: {max_beauty} <{L} {M} {H}>")


(T,) = get_ints()
for i in range(T):
    main(i + 1)
