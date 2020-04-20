#!/usr/bin/env python
import sys

fin = sys.argv[1]
fspec = sys.argv[2]

spec = dict([line.strip().split(': ') for line in open(fspec)])
aunts = []
for line in open(fin):
    aunts.append(
        dict([
            element.split(': ')
            for element in line.strip().split(': ', maxsplit=1)[1].split(', ')
        ]))


def pred(a):
    for thing in a:
        if thing in ['cats', 'trees']:
            if a[thing] <= spec[thing]:
                return False
        elif thing in ['pomeranians', 'goldfish']:
            if a[thing] >= spec[thing]:
                return False
        else:
            if a[thing] != spec[thing]:
                return False
    return True


for i, a in enumerate(aunts):
    if pred(a):
        print(i + 1)
        break
