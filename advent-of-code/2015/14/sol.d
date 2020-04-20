#!/usr/bin/env -S rdmd -g

// immutable int checkpoint = 1000;
immutable int checkpoint = 2503;
void main()
{
    Reindeer[] dear = stdin.byLine.map!parse.array;

    void part1()
    {
        int[] distances = dear.map!((ref d) => calcDistance(d, checkpoint)).array;
        size_t winnerIndex = maxIndex(distances);
        Reindeer* winner = &dear[winnerIndex];
        writefln("Part 1: %s %s", distances[winnerIndex], &winner);
    }

    void part2()
    {
        Status[] statuses = dear.map!fromDear.array;

        foreach (time; 0 .. checkpoint)
        {
            foreach (ref s; statuses)
            {
                s.update(time);
            }
            statuses.schwartzSort!(s => s.distance);

            int maxDistance = statuses[$ - 1].distance;
            foreach (ref s; statuses.retro)
            {
                // all tied lead get score
                if (s.distance == maxDistance)
                    ++s.score;
                else
                    break;
            }
            // writeln(time, " ", statuses);
        }
        writeln("Part 2: ", statuses.maxElement!(s => s.score).score);
    }

    part1;
    part2;

}

struct Reindeer
{
    string name;
    int speed;
    int fly;
    int rest;
}

Status fromDear(ref Reindeer d)
{
    return Status(&d);
}

struct Status
{
    Reindeer* dear;
    int distance;
    int score;
    alias dear this;

    void update(int time)
    {
        if (time % (fly + rest) < fly)
            distance += speed;
    }
    string toString()
    {
        return format!"%s %d#%d"(this.name, this.distance, this.score);
    }
}

import std.format;
import std.stdio;
import std.algorithm;
import std.range;

int calcDistance(ref Reindeer d, int checkpoint)
{
    int cycles = checkpoint / (d.fly + d.rest);
    int remainder = min(checkpoint % (d.fly + d.rest), d.fly);
    return (remainder + cycles * d.fly) * d.speed;
}

immutable string lineTemplate = "%s can fly %d km/s for %d seconds, but then must rest for %d seconds.";

Reindeer parse(char[] line)
{
    auto r = Reindeer();
    line.formattedRead!lineTemplate(r.name, r.speed, r.fly, r.rest);
    return r;
}
