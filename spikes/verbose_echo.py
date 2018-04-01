#!/usr/bin/env python3
from sys import argv
from sys import stdin
from sys import stdout

alp = len(argv)
if alp > 1 and argv[1] == "--version":
    print ('version 0.2')
    quit()

if alp > 1 and argv[1] == "--help":
    print ('ctrl+d to quit')
    quit()

for line in stdin:
    print (line, end='')
    stdout.flush()

print('goodbye')
stdout.flush()
