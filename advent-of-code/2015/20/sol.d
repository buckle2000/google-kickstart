#!/usr/bin/env -S rdmd -g
int divSum(int n)
{
    // Sum of divisors 
    int result = 0;

    // find all divisors which divides 'num' 
    for (int i = 2; i * i <= n; i++)
    {
        // if 'i' is divisor of 'n' 
        if (n % i == 0)
        {
            // if both divisors are same 
            // then add it once else add 
            // both 
            if (i == (n / i))
                result += i;
            else
                result += (i + n / i);
        }
    }

    return (result + n + 1);
}

int divSum2(int n, int maxHouse)
{
    // Sum of divisors 
    int result = 0;

    // find all divisors which divides 'num' 
    for (int i = 2; i * i <= n && i <= maxHouse; i++)
    {
        // if 'i' is divisor of 'n' 
        if (n % i == 0)
        {
            // if both divisors are same 
            // then add it once else add 
            // both 
            if (i == (n / i))
                result += i;
            else
            {
                result += n / i;
                if (n / i <= maxHouse)
                    result += i;
            }
        }
    }

    return (result + n + 1);
}

// Driver program to run the case 
void main()
{
    writeln(divSum(4));
    // part1;
    part2;
}

void part2()
{
    foreach (i; 0 .. int.max)
    {
        if (divSum2(i, 50) * 11 >= 34000000)
        {
            writefln("%s %s", i, divSum(i));
            break;
        }
    }
}

void part1()
{
    foreach (i; 0 .. int.max)
    {
        if (divSum(i) * 10 >= 34000000)
        {
            writefln("%s %s", i, divSum(i));
            break;
        }
    }
}

import std.stdio;
import std.conv;
