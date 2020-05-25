int solve() { // for lowest gap after inserting K
    int n, k;
    readln.formattedRead!"%d %d"(n, k);
    int[] m = readln.split.map!(to!int).array;
    auto gaps = iota(n-1).map!(i => m[i+1] - m[i]).array.heapify;
    foreach (i; 0..k) {
        int largest = gaps.front;
        gaps.popFront();
        int half = largest / 2;
        gaps.insert(half);
        gaps.insert(largest - half);
    }
    return gaps.front;
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