unittest
{
    import sol: generateMix;
    import fluent.asserts;
    import std.range;

    Assert.equal(generateMix(4, 3).array, [
        [0, 0, 0, 3],
        [0, 0, 1, 2],
        [0, 0, 2, 1],
        [0, 0, 3, 0],
        [0, 1, 0, 2],
        [0, 1, 1, 1],
        [0, 1, 2, 0],
        [0, 2, 0, 1],
        [0, 2, 1, 0],
        [0, 3, 0, 0],
        [1, 0, 0, 2],
        [1, 0, 1, 1],
        [1, 0, 2, 0],
        [1, 1, 0, 1],
        [1, 1, 1, 0],
        [1, 2, 0, 0],
        [2, 0, 0, 1],
        [2, 0, 1, 0],
        [2, 1, 0, 0],
        [3, 0, 0, 0],
    ]);
}