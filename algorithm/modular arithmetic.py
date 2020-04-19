def powmod(b, e, m):
    """Calculate b ** e (mod m)"""
    r = 1
    while e != 0:
        if e % 2 != 0: r = r * b % m
        e //= 2
        b = b * b % m
    return r

def invmod(b, m):
    """Calculate modular inverse of b (mod m)"""
    return powmod(b, m-2, m)

def divmod(a, b, m):
    """Calculate a / b (mod m)
    m must be prime
    """
    return a * invmod(b, m) % m
