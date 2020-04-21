#!/usr/bin/env -S rdmd -g

enum InstructionType
{
    Half,
    Triple,
    Increment,
    Jump,
    JumpIfEven,
    JumpIfOne,
}

struct Instruction
{
    size_t r;
    sizediff_t offset;
    InstructionType type;
}

struct Program
{
    Instruction[] instructions;
    size_t pc;
    uint[2] registers;

    bool step()
    {
        if (pc < 0 || pc >= instructions.length)
            return false;
        auto ins = instructions[pc];
        switch (ins.type) with (InstructionType)
        {
        case Half:
            registers[ins.r] /= 2;
            break;
        case Triple:
            registers[ins.r] *= 3;
            break;
        case Increment:
            registers[ins.r] += 1;
            break;
        case Jump:
            pc += ins.offset;
            goto jump;
            break;
        case JumpIfEven:
            if (registers[ins.r] % 2 == 0)
                goto case Jump;
            break;
        case JumpIfOne:
            if (registers[ins.r] == 1)
                goto case Jump;
            break;
        default:
            assert(0, "%s\n%s".format(ins, this));
        }
        ++pc;
    jump:
        // writeln(ins);
        // if (pc == 41)
        // {
        //     writeln(this.registers);
        // }
        return true;
    }
}

import std.regex;
import std.format;
import std.stdio;
import std.algorithm;
import std.range;
import std.conv;

immutable auto r = ctRegex!r"(\w+) ([ab])?(?:, )?([+-]\d+)?";

Instruction parse(string line)
{
    auto match = line.matchFirst(r);
    with (InstructionType)
    {
        sizediff_t offset;
        try
        {
            offset = to!sizediff_t(match[3]);
        }
        catch (ConvException)
        {
        }
        Instruction ins = {
            type: [
                "tpl": Triple,
                "hlf": Half,
                "inc": Increment,
                "jmp": Jump,
                "jie": JumpIfEven,
                "jio": JumpIfOne,
            ][match[1]], r: ["": -1, "a": 0, "b": 1][match[2]], offset: offset
        };
        return ins;
    }
}

void main()
{
    auto instructions = stdin.byLineCopy.map!parse.array;
    auto program = Program(instructions);
    // foreach (i; 0 .. 100)
    //     program.step();
    while (program.step) {}
    writeln("Part 1: ", program.registers[1]);

    program.pc = 0;
    program.registers = [1, 0];
    while (program.step) {}
    writeln("Part 2: ", program.registers[1]);
}
