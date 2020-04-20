#!/usr/bin/env python
import sys


def numfit(containers, total):
    assert len(containers) > 0
    if total == 0:
        return 1
    if len(containers) == 1:
        if total == containers[0]:
            return 1
        else:
            return 0
    else:
        cc = containers[1:]
        return numfit(cc, total) + numfit(cc, total - containers[0])


def bestfit(containers, total):
    assert len(containers) > 0
    if total == 0:
        return [0]
    if len(containers) == 1:
        if total == containers[0]:
            return [1]
        else:
            return []
    else:
        cc = containers[1:]
        return bestfit(cc, total) +\
        [i+1 for i in bestfit(cc, total - containers[0])]


# containers = [20,15,10,5,5]
# print(numfit(containers, 25))

# containers = list(map(int, open(sys.argv[1])))
# print(numfit(containers, 150))



S, containers = 25, [20, 15, 10, 5, 5]

# S, containers = 150, list(map(int, open(sys.argv[1])))

r = bestfit(containers, S)
print(r.count(min(r)))
