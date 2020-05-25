int maxBeauty(int[][] plates, int p) {
    if (p == 0) return 0;
    int beauty = 0;
    foreach(i; plates.length.iota) {
        if (plates[i].length > 0) {
            auto cl = plates.array;
            const int first = cl[i][0];
            cl[i] = cl[i][1..$];
            beauty = max(beauty, first + maxBeauty(cl, p-1));
        }
    }
    return beauty;
}

int solve() {
    int k, n, p;
    readln.formattedRead!"%d %d %d"(n, k, p);
    //plates
    auto x = new int[][](n, k);
    foreach (i; 0..n) {
        readln.split.map!(to!int).copy(x[i]);
    }
    return maxBeauty(x, p);
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