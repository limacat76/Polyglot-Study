#!/usr/bin/env python3
import unittest
from pexpect import spawn

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.child = spawn('python/001-fizzbuzz.py')
        self.child.setecho(False)

    def tearDown(self):
        self.child.sendeof()

    def callChild(self, xS):
        self.child.sendline (xS)
        x = self.child.readline()
        return x[:-2].decode()

    def test_number(self):
        self.assertEqual('1', self.callChild('1'))

    def test_fizz(self):
        self.assertEqual('Fizz', self.callChild('3'))

    def test_buzz(self):
        self.assertEqual('Buzz', self.callChild('5'))

    def test_fizzBuzz(self):
        self.assertEqual('FizzBuzz', self.callChild('15'))

    def test_nan(self):
        self.assertEqual('NaN', self.callChild('15x'))

if __name__ == '__main__':
    unittest.main()
