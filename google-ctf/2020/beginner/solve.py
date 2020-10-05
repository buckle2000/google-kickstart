from z3 import *

def to_z3(s):
    b = bytes.fromhex(s)
    i = int.from_bytes(b, 'little')
    return BitVecVal(i, 32*4)

solver = Solver()

def inspect(z):
    return int.to_bytes(simplify(z).as_long(), 16, 'little')

# flag = BitVecVal(int.from_bytes(b'CTF{S1MDf0rM3!}\0', 'little'), 8*16)
flag = BitVec('flag', 8*16)
# CTF{oooooooooo}\0
# 0123456789abcdef

# shuffle:
c_shuffle = bytes.fromhex("0206 0701 050b 090e 030f 0408 0a0c 0d00")

template_1 = [None] * 16
for i, idx in enumerate(c_shuffle):
    low = 8 * idx
    high = low + 7
    template_1[i] = Extract(high, low, flag)

flag_1 = Concat(*reversed(template_1))

# add32: (little-endian, carry within every 4 bytes)
c_add32 = to_z3("efbe adde adde e1fe 3713 3713 6674 6367")

template_2 = [None] * 4
for i in range(4):
    low = 32 * i
    high = low + 31
    template_2[i] = Extract(high, low, flag_1) + Extract(high, low, c_add32)

flag_2 = Concat(*reversed(template_2))

# xor:
c_xor = to_z3("7658 b449 8d1a 5f38 d423 f834 eb86 f9aa")

flag_3 = flag_2 ^ c_xor

solver.add(flag_3 == flag)
print(solver.check())
print(inspect(solver.model()[flag]))