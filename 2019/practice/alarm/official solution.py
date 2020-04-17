def get_ints():
    return map(int, input().split())

def fast_exp(b, e, m):
    r = 1
    while e:
        if e & 1: r = (r * b) % m
        e >>= 1
        b = (b * b) % m
    return r

def main(case_id):
    # N: length of A
    # K: 1...Kth power to sum up
    # A: array

    N, K, x, y, C, D, Ex, Ey, F = get_ints()
    x, y, A = [x], [y], [(x + y) % F]
    for _ in range(N - 1):
        x_next = (C * x[-1] + D * y[-1] + Ex) % F
        y_next = (C * y[-1] + D * x[-1] + Ey) % F
        x.append(x_next)
        y.append(y_next)
        A.append((x_next + y_next) % F)
    assert len(A) == N

    # # naive implementation
    # result = 0
    # for k in range(1, K+1):
    #     for L in range(N):
    #         for R in range(L, N):
    #             for j in range(L, R+1):
    #                 result = result + A[j] * pow(j-L+1, k)
    #                 result %= 1000000007

    # Copied from https://github.com/wachino/google-kick-start-2019/blob/master/Practice%20Round/Kickstart%20Alarm/solution.cpp
    ans = 0
    la = K
    mod = 1000000007
    for i in range(N):
        ans += la * (N - i) * A[i]
        ans %= mod
        xx = (fast_exp(i+2, K+1, mod) - 1) * fast_exp(i+1, mod-2, mod) - 1
        la += xx
        la %= mod
    result = ans
    
    print("Case #{}: {}".format(case_id, result))
    # print("Case #{} {}: {}".format(case_id, A, result))
    # print("Powers:", powers)


(T,) = get_ints()
for i in range(T):
    main(i + 1)
