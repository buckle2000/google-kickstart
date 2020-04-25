import sys

# possible = 0
# for line in sys.stdin:
#     sides = list(map(int, line.split()))
#     sides.sort()
#     if sides[0] + sides[1] > sides[2]:
#         possible+=1
# print(possible)


possible = 0
triangles = []
for line in sys.stdin:
    sides = list(map(int, line.split()))
    triangles.append(sides)

possible = 0
for x in range(3):
    for y0 in range(0, len(triangles), 3):
        sides = [triangles[y0][x], triangles[y0 + 1][x], triangles[y0 + 2][x]]
        sides.sort()
        if sides[0] + sides[1] > sides[2]:
            possible += 1
print(possible)
