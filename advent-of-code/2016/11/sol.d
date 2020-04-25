#!/usr/bin/env -S rdmd -g

enum ItemType
{
    Chip,
    Generator
}

struct Item
{
    ItemType type;
    size_t element;
}

struct State(size_t Nfloor, size_t Nelement, size_t elevatorCapacity = 2)
{
    size_t elevatorFloor;
    bool[Nelement][Nfloor] chips;
    bool[Nelement][Nfloor] generators;

    bool validate() const
    {
        return _validate;
    }

    void move(sizediff_t direction, const Item[elevatorCapacity] items) nothrow
    {
        assert(direction == -1 || direction == 1);
        const auto nextFloor = elevatorFloor + direction;
        foreach (ref item; items)
        {
            final switch (item.type)
            {
            case ItemType.Chip:
                chips[elevatorFloor][item.element] = false;
                chips[nextFloor][item.element] = true;
                break;
            case ItemType.Generator:
                generators[elevatorFloor][item.element] = false;
                generators[nextFloor][item.element] = true;
                break;
            }
        }
        elevatorFloor = nextFloor;
    }

    invariant(_validate);
    private bool _validate() const
    {
        if (elevatorFloor < 0 || elevatorFloor >= Nfloor)
            return false;
        bool[Nelement] hasThis;
        foreach (floor; chips)
            hasThis[] &= floor[];
        foreach (count; hasThis)
            if (count != 1)
                return false;
        return true;
    }
}

import std.range;
import std.algorithm;
import std.container;
void main()
{
    immutable State!(4, 5) puzzle = {
        // cu pl ru st th
        chips: [
            [0, 1, 0, 1, 0], [1, 0, 1, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0],
        ], generators: [
            [0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
        ],
    };
    Set
    // puzzle.valid;
}
