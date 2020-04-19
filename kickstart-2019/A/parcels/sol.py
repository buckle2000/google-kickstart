def get_ints():
    return tuple(map(int, input().split()))


# import math
import numpy as np
from scipy.signal import convolve2d


def flood(matrix):
    return convolve2d(matrix, [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0],
    ], mode='same').astype(bool)


# False are shadow


def lux(x):
    """Amount of light with radius of `distance`

    0 => 1
        x

    1 => 5
        x
       xxx
        x

    2 => 13
        x
       xxx
      xxxxx
       xxx
        x
    """
    return 1 + 2 * x * (x + 1)


def try_light_all(matrix, luminosity, shade):
    if shade == 0:
        return True

    unlit = set()
    for idx, value in np.ndenumerate(matrix):
        if not value:
            unlit.add(idx)
    unlit_np = np.array(list(unlit))
    bmax = unlit_np.max(axis=0)
    bmin = unlit_np.min(axis=0)
    bounds = bmax - bmin

    # too fair apart
    if bounds[0] > luminosity * 2 or bounds[1] > luminosity * 2:
        return False


    # print(bmin[0] + luminosity, bmax[0] - luminosity + 1)
    for xx in range(bmax[0] - luminosity, bmin[0] + luminosity + 1):
        for yy in range(bmax[1] - luminosity, bmin[1] + luminosity + 1):
            lit_squares = 0
            for x in range(-luminosity, luminosity + 1):
                for y in range(-luminosity, luminosity + 1):
                    if abs(x) + abs(y) <= luminosity and\
                        (xx+x, yy+y) in unlit:
                        # 0 <= xx+x < matrix.shape[0] and\
                        # 0 <= yy+y < matrix.shape[1] and\
                        lit_squares += 1
                        # print(xx+x, yy+y)
            if lit_squares > shade:
                raise ValueError("WTF")
            if lit_squares >= shade:
                return True

    return False


def main(matrix):
    luminosity = 0
    while True:
        shade = matrix.size - matrix.sum()  # amount of "holes"
        # print(lux(luminosity), shade, matrix)
        if lux(luminosity) >= shade:  # heuristic skip
            if try_light_all(matrix, luminosity, shade):
                break
        luminosity += 1
        matrix = flood(matrix)
    # print(matrix)
    # print(flood(matrix))
    return luminosity


T, = get_ints()
for i in range(T):
    shape = get_ints()
    array = np.ndarray(shape, dtype=bool)
    for j in range(shape[0]):
        array[j] = tuple(map(int, input()))
    # print(array)
    ans = main(array)
    print("Case #{}: {}".format(i + 1, ans))
