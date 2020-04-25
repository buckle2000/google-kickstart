import sys


def xxx(x, min_, max_):
    return max(min(x, max_), min_)

def solve(keypad, pos):
    keycode = ''
    for line in sys.stdin:
        for c in line.strip():
            lastpos = pos
            pos += {
                'U': -1j,
                'D': 1j,
                'L': -1,
                'R': 1,
            }[c]
            if pos not in keypad:
                pos = lastpos
        keycode += keypad[pos]
    print(keycode)

# solve({
#     0+0j: '1',
#     1+0j: '2',
#     2+0j: '3',
#     0+1j: '4',
#     1+1j: '5',
#     2+1j: '6',
#     0+2j: '7',
#     1+2j: '8',
#     2+2j: '9',
# }, 1+1j)


solve({
    0j+2: '1',
    1j+1: '2',
    1j+2: '3',
    1j+3: '4',
    2j+0: '5',
    2j+1: '6',
    2j+2: '7',
    2j+3: '8',
    2j+4: '9',
    3j+1: 'A',
    3j+2: 'B',
    3j+3: 'C',
    4j+2: 'D',
}, 2j+0)
