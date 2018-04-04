import unittest
from pexpect import spawn

class BaseTest(unittest.TestCase):

    def spawnFile(self):
        raise ValueError('What subprogram are you trying to test?')

    def setUp(self):
        self.child = spawn(self.spawnFile())
        self.child.setecho(False)

    def tearDown(self):
        self.child.sendeof()

    def callChild(self, xS):
        self.child.sendline (xS)
        x = self.child.readline()
        return x[:-2].decode()