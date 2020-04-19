import random

T = 1
print(T)
N = 1000000
Q = 300
for _ in range(T):
    print(N, Q)
    for _ in range(Q):
        begin = random.randrange(N)
        end = random.randrange(begin, N)
        print(begin, end)
