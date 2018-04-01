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

print('basic pexpect testing')
child = spawn('echo ciao')
child.expect('ciao')
child = spawn('echo bau')
child.expect('bau')
child = spawn('echo bau2')
child.expect('bau')

print('testing the call of a self-contained-script in python')
child = spawn('./verbose_echo.py')
child.sendline ('aaa')
child.expect('aaa')
child.sendline ('')
child.sendeof()
child.expect('goodbye')

print('testing the call of fizzbuzz')
child = spawn('../python/001-fizzbuzz.py')
child.sendline ('1')
child.expect('1')
child.sendline ('3')
child.expect('Fizz')
child.sendline ('5')
child.expect('Buzz')
child.sendline ('15')
child.expect('FizzBuzz')
child.sendline ('something')
child.expect('NaN')
child.sendline ('')
child.sendeof()
print('testing the call of fizzbuzz with a mistake')
child = spawn('../python/001-fizzbuzz.py')
child.setecho(False)
child.sendline ('1')
child.expect('')
x = child.readline()
print (x[:-2].decode())
child.sendline ('something')
x = child.readline()
print (x[:-2].decode())
child.sendline ('5')
x = child.readline()
print (x[:-2].decode())
child.sendeof()
