def get_ints():
    return map(int, input().split())

CHUNK_SIZE = 1 << 0x10

def calc_beauty(wall, L, H):
    """Naive"""
    return sum(wall[L : H + 1])

def main(case_id):
    input()
    wall = input()
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
    print("Case #{}: {}".format(case_id, max_beauty))
    # print(f"Case #{case_id}: {max_beauty} <{L} {M} {H}>")


(T,) = get_ints()
for i in range(T):
    main(i + 1)
