from collections import Counter
import sys, re
import string


real = 0
real_sectors = []
for line in sys.stdin:
    match = re.match(r"(.*)-(\d+)\[(.*)\]", line)
    name = match[1]
    sector = int(match[2])
    common = match[3]
    c = Counter(sorted(x for x in name if x in string.ascii_lowercase))
    if "".join(x[0] for x in c.most_common(5)) == common:
        real += sector
        real_sectors.append((name, sector))
print(real)


def shift(s, forward_by):
    return "".join(
        chr((ord(c) - ord("a") + forward_by) % 26 + ord("a"))
        if c in string.ascii_lowercase
        else c
        for c in s
    )


for name, sector in real_sectors:
    name = shift(name, sector)
    print(sector, name)
