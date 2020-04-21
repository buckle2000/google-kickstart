#!/usr/bin/env python


def location(x, y):
    """
    >>> location(1, 1)
    1
    >>> location(3, 3)
    13
    >>> location(5, 2)
    20
    >>> location(2, 4)
    12
    """
    yinc = x
    base = ((1 + x) * x) // 2
    return base + ((2*yinc + y-2) * (y-1)) // 2
    # return 1 + 2 * x + (y - 1) * (y - 1) // 2


def powmod(b, e, m):
    """Calculate b ** e (mod m)"""
    r = 1
    while e != 0:
        if e % 2 != 0: r = r * b % m
        e //= 2
        b = b * b % m
    return r


if __name__ == "__main__":
    x = 3029
    y = 2947
    e = location(x, y)
    ans = 20151125 * powmod(252533, e - 1, 33554393) % 33554393
    print(ans)