#!/usr/bin/env python
import numpy as np
import sys
import re

fin = sys.argv[1]

replacements, molecule = open(fin).read().split('\n\n')
replacements = [line.split(' => ') for line in replacements.splitlines(False)]
molecule = molecule.strip()

def transform(molecule, result=None):
    if result is None:
        result = set()
    for before, after in replacements:
        for match in re.finditer(before, molecule):
            transformed = molecule[:match.start()] + after + molecule[match.
                                                                      end():]
            result.add(transformed)
        # print(transformed)
    return result


# print(replacements)
# print(molecule)

# Part 1
# print(len(transform(molecule)))

# Part 2


def untransform(m, molecule, result=None):
    if result is None:
        result = set()
    for after, before in m:
        for match in re.finditer(before, molecule):
            transformed = molecule[:match.start()] + after + molecule[match.
                                                                      end():]
            result.add(transformed)
        # print(transformed)
    return result


withRn = [(before, after) for (before, after) in replacements if 'Rn' in after]


def dothis(m, molecule):
    generations = [{molecule}]
    while len(generations[-1]) > 0:
        next_generation = set()
        for before in generations[-1]:
            untransform(withRn, before, next_generation)
        for g in generations:
            next_generation -= g
        print('Generation', len(generations), len(next_generation))
        generations.append(next_generation)
    return generations[-2]

atoms = [m.group() for m in re.finditer("[A-Ze][a-z]?", molecule)]
print(atoms)
steps = len(atoms) - 1 - 2 * atoms.count('Y') - 2 * atoms.count('Ar')
print(steps)
