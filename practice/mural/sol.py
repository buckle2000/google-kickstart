def get_ints():
    return map(int, input().split())

def calc_beauty(wall, L, H):
    """Naive"""
    return sum(wall[L : H + 1])

def main(case_id):
    input()
    wall = input()
    wall = list(map(int, wall))
    N = len(wall)
    max_beauty = 0
    def calc_h(L):
        return N - N // 2 + L - 1

    beauty = None

    for L in range(0, N//2+1):
        H = calc_h(L)
        if beauty is None:
            beauty = calc_beauty(wall, L, H)
        else:
            beauty = beauty - wall[L-1] + wall[H]
        max_beauty = max(beauty, max_beauty)
    print("Case #{}: {}".format(case_id, max_beauty))

(T,) = get_ints()
for i in range(T):
    main(i + 1)
