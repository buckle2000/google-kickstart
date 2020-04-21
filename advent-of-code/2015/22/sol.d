#!/usr/bin/env -S rdmd -g

struct Spell
{
    string name = "Unnamed";
    int cost;
    int duration = 1;
    int damage = 0;
    int heal = 0;
    int shield = 0;
    int recharge = 0;
}

immutable Spell[] spells = [
    {name: "Magic Missile", cost: 53, damage: 4},
    {name: "Drain", cost: 73, damage: 2, heal: 2},
    {name: "Shield", cost: 113, duration: 6, shield: 7},
    {name: "Poison", cost: 173, duration: 6, damage: 3},
    {name: "Recharge", cost: 229, duration: 5, recharge: 101},
];

import std.random;
import std.range;

enum GameResult
{
    Continue,
    Win,
    Lose,
}

immutable check = "
    debug writeln(this);
    if (auto result = tryTerminate)
        return result;
";

struct Game
{
    int hp;
    int mana;
    int armor;
    int bossHp;
    int bossDamage;
    int manaUsed = 0;
    int attrition = 0;
    size_t[] choices;

    int[spells.length] activeSpells;

    alias Result = GameResult;
    alias Result this;

    void handleSpells()
    {
        armor = 0;
        foreach (i, ref timer; activeSpells)
        {
            if (timer == 0)
                continue;
            hp += spells[i].heal;
            mana += spells[i].recharge;
            armor += spells[i].shield;
            bossHp -= spells[i].damage;

            --timer;
        }
    }

    bool validSpell(size_t spellIndex)
    {
        auto x = spells[spellIndex];
        return x.cost <= mana && activeSpells[spellIndex] == 0;
    }

    size_t randomSpell()
    {
        size_t[] affordableSpells = spells.length.iota.filter!(i => validSpell(i)).array;
        if (affordableSpells.length == 0)
        {
            debug writeln("You ran out of mana. You lose.");
            return Lose;
        }
        return affordableSpells[].choice;
    }

    bool castSpell(size_t spellIndex)
    {
        if (!validSpell(spellIndex))
            return false;
        Spell spell = spells[spellIndex];
        debug writefln("Cast %s", spell.name);
        mana -= spell.cost;
        manaUsed += spell.cost;
        activeSpells[spellIndex] = spell.duration;
        return true;
    }

    Result phasePrecheck()
    {
        hp -= attrition;
        mixin(check);
        handleSpells;
        mixin(check);
        debug writeln("Player turn");
        return Continue;
    }

    Result phaseBoss()
    {
        handleSpells;
        mixin(check);
        debug writeln("Boss turn");
        hp -= max(1, bossDamage - armor);
        mixin(check);
        return Continue;
    }

    Result step(size_t spellIndex)
    {
        if (!castSpell(spellIndex))
            return Lose;

        if (auto result = phaseBoss)
            return result;

        if (auto result = phasePrecheck)
            return result;

        return Continue;
    }

    Result runRandom()
    {
        while (true)
        {
            if (auto result = step(randomSpell))
                return result;
        }
    }

    Result tryTerminate()
    {
        if (hp <= 0 || mana <= 0)
        {
            debug writeln("You lose.");
            return Lose;
        }
        if (bossHp <= 0)
        {
            debug writeln("You win.");
            return Win;
        }
        return Continue;
    }
}

import core.thread;

void main()
{
    part1;
    part2;
}

void part1()
{
    int minManaUsed = int.max;
    scope (exit)
    {
        if (minManaUsed == int.max)
            writeln("Part 1: No solution");
        else
            writeln("Part 1: ", minManaUsed);
    }

    foreach (_; 0 .. 1000000)
    {
        Game game = {hp: 50, mana: 500, bossHp: 71, bossDamage: 10};
        if (game.runRandom() == GameResult.Win)
        {
            minManaUsed = min(minManaUsed, game.manaUsed);
        }
    }
}

int BFS(Game game, int minManaUsed = int.max)
{
    foreach (i; 0 .. spells.length)
    {
        Game copy = game;
        switch (copy.step(i)) with (GameResult)
        {
        case Win:
            minManaUsed = min(minManaUsed, copy.manaUsed);
            break;
        case Continue:
            minManaUsed = min(minManaUsed, BFS(copy));
            break;
        case Lose:
        default:
            break;
        }
    }
    return minManaUsed;
}

void part2()
{
    Game game = {hp: 50, mana: 500, bossHp: 71, bossDamage: 10};
    game.attrition = 1;

    immutable int minManaUsed = BFS(game);
    if (minManaUsed == int.max)
        writeln("Part 2: No solution");
    else
        writeln("Part 2: ", minManaUsed);
}

import std.stdio;
import std.conv;
import std.algorithm;
