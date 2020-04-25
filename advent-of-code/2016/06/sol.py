import sys
from collections import Counter


def ha():
    for line in sys.stdin:
        yield list(line.strip())


grid = list(ha())
# print(grid[0])
counters = [Counter(line[i] for line in grid) for i in range(len(grid[0]))]
print("".join([c.most_common(1)[0][0] for c in counters]))
print("".join([c.most_common()[-1][0] for c in counters]))

# python is so garbage for data-oriented programming