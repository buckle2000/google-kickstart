#!/usr/bin/env -S rdmd -g
int getY(ref Event e)
{
    if (e.isEnd)
        return e.y2;
    else
        return e.y1;
}

void main()
{
    int N;
    readf("%d\n", N);
    auto rectangles = new Rectangle[N];
    auto events = new Event[N * 2]; // ys
    auto breakpoints = new int[N * 2]; // xs
    foreach (i, ref r; rectangles)
    {
        readf("%d %d\n", r.x1, r.y1);
        readf("%d %d\n", r.x2, r.y2);
        events[i * 2].rectangle = &r;
        events[i * 2].isEnd = false;
        events[i * 2 + 1].rectangle = &r;
        events[i * 2 + 1].isEnd = true;
        breakpoints[i * 2] = r.x1;
        breakpoints[i * 2 + 1] = r.x2;
    }
    events.sort!((a, b) => getY(a) < getY(b));
    breakpoints.sort;

    // writeln(rectangles);
    // writeln(events.map!(x => x.isEnd));
    // writeln(events.map!(x => *x.rectangle));
    // writeln(breakpoints);

    int ans = 0;

    foreach (i; 1 .. breakpoints.length)
    {
        int x1 = breakpoints[i - 1];
        int x2 = breakpoints[i];
        if (x1 == x2)
            continue;

        int onStack = 0; // rectangles opened but not closed
        int lastOpen; // last event to make onStack > 0
        int sum = 0; // length (y) cummulated so far (in this section)
        foreach (ref e; events)
        {
            bool inScope = e.x1 < x2 && e.x2 > x1;
            if (inScope)
            {
                if (e.isEnd)
                {
                    --onStack;
                    if (onStack == 0)
                        sum += (e.y2 - lastOpen);
                }
                else
                {
                    if (onStack == 0)
                        lastOpen = e.y1;
                    ++onStack;
                }

            }
            assert(onStack >= 0);
        }
        ans += sum * (x2 - x1);
    }

    writeln(ans);
}

import std.stdio;
import std.algorithm;

struct Event
{
    Rectangle* rectangle;
    alias rectangle this;
    bool isEnd;
}

struct Rectangle
{
    int x1;
    int x2;
    int y1;
    int y2;
}
