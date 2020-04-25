from in_ import *

outputs = {}

def handle_set(_type, _id, x):
    if _type is BOT:
        bots[_id].append(x)
    elif _type is OUTPUT:
        outputs[_id] = x
    else:
        raise NotImplementedError(_type, _id, x)

change = True
while change:
    change = False
    keys = list(bots.keys())
    for bot_id in keys:
        chips = bots[bot_id]
        assert len(chips) <= 2
        if len(chips) == 2:
            change = True
            bots[bot_id] = []
            smaller = min(chips)
            larger = max(chips)
            # print(bot_id, smaller, larger)
            if smaller == 17 and larger == 61:
                print("Part 1:", bot_id)
            smaller_type, smaller_id = dest[bot_id][0]
            larger_type, larger_id = dest[bot_id][1]
            handle_set(smaller_type, smaller_id, smaller)
            handle_set(larger_type, larger_id, larger)

print("Part 2:", outputs[0] * outputs[1] * outputs[2])
