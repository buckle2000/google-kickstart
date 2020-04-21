#!/usr/bin/env -S rdmd -g

import std.format;
import std.stdio;
import std.algorithm;
import std.range;
import std.conv;
import std.concurrency;

ulong parse(string line)
{
    return to!ulong(line);
}

InputRange!(ulong[]) combinations(const ulong[] packages, const ulong sum)
{
    return new Generator!(ulong[])({
        if (sum == 0)
        {
            yield(cast(ulong[])[]);
            return;
        }
        foreach (i, p; packages)
        {
            if (p <= sum)
            {
                foreach (c; combinations(packages[i + 1 .. $], sum - p))
                    yield([p] ~ c);
            }
        }
    });
}

void main()
{
    auto packages = stdin.byLineCopy.map!parse.array;

    void solve(ulong parts)
    {
        ulong minQuantum = ulong.max;
        size_t shortestLength = size_t.max;
        foreach (c; combinations(packages, packages.sum / parts))
        {
            if (c.length < shortestLength)
            {
                shortestLength = c.length;
                const ulong quantum = c.reduce!`a*b`;
                minQuantum = quantum;
                writefln("%s %s", minQuantum, shortestLength);
            }
            else if (c.length == shortestLength)
            {
                const ulong quantum = c.reduce!`a*b`;
                if (quantum < minQuantum)
                {
                    minQuantum = quantum;
                    writefln("%s %s", minQuantum, shortestLength);
                }
            }
        }
    }
    // solve(3);
    // writeln("Part 1 Done.");
    solve(4);
    writeln("Part 2 Done.");
}
