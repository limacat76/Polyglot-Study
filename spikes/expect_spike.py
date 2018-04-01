#!/usr/bin/env python3
from sys import argv
from sys import stdin
from sys import stdout
from pexpect import spawn

alp = len(argv)
if alp > 1 and argv[1] == "--version":
    print ('version 0.1')
    quit()

if alp > 1 and argv[1] == "--help":
    print ('ctrl+d to quit')
    quit()

child = spawn('echo ciao')
child.expect('ciao')
child = spawn('echo bau')
child.expect('bau')
child = spawn('echo bau2')
child.expect('bau')
print('testing the call of a self-contained-script in python')
child = spawn('./verbose_echo.py')
child.send('aaa\n')
child.expect('aaa')
child.send('\n')
child.sendeof()
child.expect('goodbye')
print('testing the call of fizzbuzz')
child = spawn('../python/001-fizzbuzz.py')
child.send('1\n')
child.expect('1')
child.send('3\n')
child.expect('Fizz')
child.send('5\n')
child.expect('Buzz')
child.send('15\n')
child.expect('FizzBuzz')
child.send('something\n')
child.expect('NaN')
child.send('\n')
child.sendeof()
