#!/usr/bin/env -S rdmd -g

immutable Item NOTHING = [0, 0, 0];
immutable Item[] weapons = [
    [8, 4, 0], // Dagger       
    [10, 5, 0], // Shortsword   
    [25, 6, 0], // Warhammer    
    [40, 7, 0], // Longsword    
    [74, 8, 0], // Greataxe     
];

immutable Item[] armors = [
    NOTHING, // Nothing
    [13, 0, 1], // Leather    
    [31, 0, 2], // Chainmail  
    [53, 0, 3], // Splintmail 
    [75, 0, 4], // Bandedmail 
    [102, 0, 5], // Platemail  
];
immutable Item[] rings = [
    NOTHING, // Nothing
    [25, 1, 0], // Damage +1  
    [50, 2, 0], // Damage +2  
    [100, 3, 0], // Damage +3  
    [20, 0, 1], // Defense +1 
    [40, 0, 2], // Defense +2 
    [80, 0, 3], // Defense +3 
];

void main()
{
    Item[] loadouts;
    foreach (w; weapons)
        foreach (a; armors)
            foreach (r0; rings)
                foreach (r1; rings)
                {
                    Item loadout = w[] + a[] + r0[] + r1[];
                    loadouts ~= loadout;
                }
    writeln("Generated");
    loadouts.schwartzSort!(x => x.cost);
    Item part1()
    {
        foreach (l; loadouts)
        {
            auto boss = Player(104, 8, 1);
            auto player = Player(100, l.damage, l.armor);

            while (true)
            {
                player.attack(boss);
                if (boss.hp <= 0)
                    return l;
                boss.attack(player);
                if (player.hp <= 0)
                    break;
            }
            // writefln("%s is not working", l);
        }
        return [9999, 9999, 9999];
    }

    writeln(part1.cost);

    Item part2()
    {
        foreach (l; loadouts)
        {
            auto boss = Player(104, 8, 1);
            auto player = Player(100, l.damage, l.armor);

            while (true)
            {
                player.attack(boss);
                if (boss.hp <= 0)
                    break;
                boss.attack(player);
                if (player.hp <= 0)
                    return l;
            }
            // writefln("%s is not working", l);
        }
        return [9999, 9999, 9999];
    }

    loadouts.schwartzSort!(x => -x.cost);
    writeln(part2.cost);
}

struct Player
{
    int hp;
    int damage;
    int armor;
    void attack(ref Player other)
    {
        other.hp -= max(1, damage - other.armor);
    }
}

alias Item = int[3];

int cost(Item x)
{
    return x[0];
}

int damage(Item x)
{
    return x[1];
}

int armor(Item x)
{
    return x[2];
}

import std.stdio;
import std.conv;
import std.algorithm;
