import sys
pos = 0+0j
dir = 1+0j

# for token in sys.stdin.read().strip().split(', '):
#     if token[0] == 'L':
#         dir *= 1j
#     elif token[0] == 'R':
#         dir *= -1j
#     else:
#         raise NotImplementedError
#     for i in range()
#     pos += int(token[1:]) * dir
print(abs(pos.imag)+abs(pos.real))


visited = {pos}
for token in sys.stdin.read().strip().split(', '):
    if token[0] == 'L':
        dir *= 1j
    elif token[0] == 'R':
        dir *= -1j
    else:
        raise NotImplementedError
    for _ in range(int(token[1:])):
        pos += dir
        if pos in visited:
            print(abs(pos.imag)+abs(pos.real))
            exit(0)
        visited.add(pos)

