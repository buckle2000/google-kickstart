from z3 import *

memory = [BitVec(f"memory_{i}", 7) for i in range(8)]

magic = Concat(
    memory[0], memory[5],
    memory[6], memory[2],
    memory[4], memory[3],
    memory[7], memory[1],
)

kittens = Concat(
    Extract( 9,  0, magic),
    Extract(41, 22, magic),
    Extract(21, 10, magic),
    Extract(55, 42, magic),
)

solver = Solver()
solver.add(kittens == 3008192072309708)
solver.check()
model = solver.model()

c_memory = ['_'] * len(memory)
for i, m in enumerate(memory):
    x = model[m].as_long()
    # x = int(bin(x)[2:].zfill(7)[::-1], 2)
    c_memory[i] = chr(x)

idx = 0
print("start")
for i in range(len(memory)):
    print(c_memory[idx], ord(c_memory[idx]))
    idx = (idx+5) % len(memory)