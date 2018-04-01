#!/usr/bin/env python3
"""write a programs that prints the number from 1 to 100, but for multiples of three prints
"Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are
multiples of three and five print "FizzBuzz"
"""

from numbers import Number
from sys import argv
from sys import stdin
from sys import stdout

def fizzBuzz(xS) :
    if isinstance(xS, str):
        if xS.isnumeric(): 
            x = int(xS)
        else:
            return "NaN"
    else: 
        x = xS

    if x % 3 == 0 and x % 5 == 0:
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return x

alp = len(argv)
if alp > 1 and argv[1] == "--version":
    print ('version 0.1')
    quit()

if alp > 1 and argv[1] == "--help":
    print ('input data')
    print ('ctrl+d to quit')
    print ('--sr for calculating 1.100 range')
    quit()

if alp > 1 and argv[1] == "--sr":
    sr = True
else:
    sr = False

if not sr:
    for line in stdin:
        value = fizzBuzz(line.strip())
        print(value)
        stdout.flush()
    stdout.close()
    stdin.close()
else:
    for x in range(1, 101):
        y = fizzBuzz(x)
        print(y)

