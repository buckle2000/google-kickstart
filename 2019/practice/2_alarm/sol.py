def get_ints():
    return map(int, input().split())


def _gen_subarray(A, N):
    for L in range(0, N):  # inclusive
        for H in range(L + 1, N + 1):  # exclusive
            yield A[L:H]


def calc_power(A, i, N):
    """Naive"""

    def _helper(subA):
        return sum(a * (p + 1) ** i for p, a in enumerate(subA))

    return sum(map(_helper, _gen_subarray(A, N)))


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
    powers = [calc_power(A, i, N) for i in range(1, K + 1)]
    power = sum(powers) % 1000000007
    print("Case #{}: {}".format(case_id, power))
    # print("Powers:", powers)
    # print(f"Case #{case_id}: {max_beauty} <{L} {M} {H}>")


(T,) = get_ints()
for i in range(T):
    main(i + 1)
