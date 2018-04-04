#!/usr/bin/env python3
import unittest
from .common import basetest
from pexpect import spawn

class TestStringMethods(basetest.BaseTest):

    def spawnFile(self):
        return 'python/002-echo.py'

    def test_equals(self):
        self.assertEqual('Prova', self.callChild('Prova'))

    def testn_not_equals(self):
        self.assertNotEqual('Fizz', self.callChild('Buzz'))

if __name__ == '__main__':
    unittest.main()
