int solve() {
    int n, b;
    readln.formattedRead!"%d %d"(n, b);
    int[] a = readln.split.map!(to!int).array;
    auto h = heapify!"a > b"(a);
    foreach (i; 0..n) {
        b -= h.front;
        h.popFront();
        if (b < 0) return i;
    }
    return n;
}

void main() {
    int t;
    readln.formattedRead!"%d"(t);
    foreach (i; 1..t+1) {
        auto ans = solve();
        writefln("Case #%d: %s", i, ans);
    }
}

import std.stdio;
import std.conv;
import std.format;
import std.range;
import std.algorithm;
import std.container.binaryheap;