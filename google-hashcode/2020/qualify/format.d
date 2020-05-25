/+ dub.sdl:
name "solution"
dependency "painlessjson" version="~>1.4.0"
+/

struct Library
{
    int signupCost;
    int scanSpeed;
    int[] books; // ID
}

void input(ref int[] bookScores, ref Library[] libraries, ref int numDay)
{
    int numBook, numLibrary;
    readln.formattedRead!"%d %d %d"(numBook, numLibrary, numDay);
    bookScores = new int[numBook];
    libraries = new Library[numLibrary];
    readln.split.map!(to!int).copy(bookScores);
    foreach (i, ref lib; libraries)
    {
        int n;
        readln.formattedRead!"%d %d %d"(n, lib.signupCost, lib.scanSpeed);
        auto bookIDs = new int[n];
        readln.split.map!(to!int).copy(bookIDs);
        lib.books = bookIDs;
    }
}

void main()
{
    int[] bookScores;
    Library[] libraries;
    int numDay;
    input(bookScores, libraries, numDay);
    write(`{"scores":`);
    write(toJSON(bookScores));
    write(`,"libraries":`);
    write(toJSON(libraries));
    write(`,"days":`);
    write(toJSON(numDay));
    write(`}`);
}

import std.stdio;
import std.conv;
import std.format;
import std.range;
import std.algorithm;
import std.json;
import painlessjson;
