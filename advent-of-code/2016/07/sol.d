#!/usr/bin/env -S rdmd -g

import std.stdio;
import std.conv;

// import std.parallelism;
import std.range;
import std.algorithm;
import std.string;
import std.concurrency;

InputRange!(char[N]) findPattern(size_t N)(const char[] ipv7, bool findInBracket,
        bool function(const char[N]) pred) if (N >= 1)
{
    bool inBracket = false;
    char[N] seq;

    void reset()
    {
        seq[] = 0;
    }

    reset;

    return new Generator!(char[N])({
        foreach (c; ipv7)
        {
            switch (c)
            {
            case '[':
                inBracket = true;
                reset;
                break;
            case ']':
                inBracket = false;
                reset;
                break;
            default:
                foreach (i; 0 .. seq.length - 1)
                {
                    seq[i] = seq[i + 1];
                }
                seq[$ - 1] = c;
                if (pred(seq))
                {
                    // writeln(seq);
                    if (inBracket == findInBracket)
                        yield(seq);
                }
                break;
            }
        }
    });
}

bool predABBA(const char[4] seq)
{
    return seq[0] == seq[3] && seq[1] == seq[2] && seq[0] != seq[1];
}

bool predABA(const char[3] seq)
{
    return seq[0] == seq[2] && seq[0] != seq[1];
}

bool supportSSL(const char[] ipv7)
{
    auto outsides = findPattern(ipv7, false, &predABA).array;
    foreach (inside; findPattern(ipv7, true, &predABA))
        foreach (outside; outsides)
        {
            if (inside[0] == outside[1] && inside[1] == outside[0])
                return true;
        }
    return false;
}

bool supportTLS(const char[] ipv7)
{
    return !findPattern(ipv7, false, &predABBA).empty && findPattern(ipv7, true, &predABBA).empty;
}

void main()
{
    const auto lines = stdin.byLineCopy.array;
    int part1 = lines.map!supportTLS.sum;
    writeln(part1);
    int part2 = lines.map!supportSSL.sum;
    writeln(part2);
}
