#!/usr/bin/env python3
import unittest
from .common import basetest
from pexpect import spawn

class TestStringMethods(basetest.BaseTest):

    def spawnFile(self):
        return 'python/001-fizzbuzz.py'

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

    def test_nan2(self):
        self.assertEqual('NaN', self.callChild('Qualcos''altro'))

if __name__ == '__main__':
    unittest.main()
