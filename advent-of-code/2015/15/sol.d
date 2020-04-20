#!/usr/bin/env -S rdmd -g

immutable int MAX_SPOON = 100;

import std.concurrency;

InputRange!(int[]) generateMix(size_t N, int sum)
in
{
    assert(N > 0);
}
do
{
    return new Generator!(int[])({
        if (N == 1)
        {
            yield([sum]);
        }
        else
        {
            foreach (int i; 0 .. sum + 1)
            {
                foreach (submix; generateMix(N - 1, sum - i))
                    yield([i] ~ submix);
            }
        }
    });
}

void main()
{
    Ingredient[] ingredients = stdin.byLine.map!parse.array;
    auto properties = ingredients.map!(x => x.properties).array;
    {
        int maxScore = 0;
        foreach (mix; generateMix(ingredients.length, MAX_SPOON))
        {
            int score = calcScore(properties, mix);
            maxScore = max(score, maxScore);
        }
        writeln("Part 1: ", maxScore);
    }
    {
        int maxScore = 0;
        foreach (mix; generateMix(ingredients.length, MAX_SPOON))
        {
            int score = calcScore!500(properties, mix);
            maxScore = max(score, maxScore);
        }
        writeln("Part 2: ", maxScore);
    }
}

import std.range;

int calcScore(int calorieLimit = 0)(IngredientProperty[] properties, int[] mix)
in
{
    assert(mix.length == properties.length, format!"%d != %d"(properties.length, mix.length));
}
do
{
    int[] sum = new int[5];
    foreach (i, ref p; properties)
    {
        int[] arr = cast(int[5]) p;
        sum[] += arr[] * mix[i];
    }
    static if (calorieLimit != 0)
    {
        if (sum[4] != 500)
            return 0;
    }
    foreach (ref s; sum)
    {
        if (s < 0)
            s = 0;
    }
    return sum[0] * sum[1] * sum[2] * sum[3];
}

import std.typecons;

alias IngredientProperty = Tuple!(int, "capacity", int, "durability", int,
        "flavor", int, "texture", int, "calories");

struct Ingredient
{
    string name;
    IngredientProperty properties;
    alias properties this;
}

Ingredient parse(char[] line)
{
    Ingredient x;
    line.formattedRead!"%s: capacity %d, durability %d, flavor %d, texture %d, calories %d"(x.name,
            x.capacity, x.durability, x.flavor, x.texture, x.calories);
    return x;
}

import std.format;
import std.stdio;
import std.algorithm;
import std.range;
