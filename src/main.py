'''
Created on Feb 25, 2010

@author: oc
'''
from DynamInt import *

import unittest

class TestDynamicIntegerOperations(unittest.TestCase):

    def setUp(self):
        self.a = DynamInt()
        self.b = DynamInt()
        self.b.setData("3241151433")
        self.a.setData("3141426236695055312")
        self.temp = DynamInt()
    def test_add(self):
        # make sure we can add
        temp = self.a+self.b
        result = "3141426239936206745"
        self.assertEqual(temp.getData(), result)

    def test_subtract(self):
        # make sure we can subtract
        temp = self.a-self.b
        result = "3141426233453903879"
        self.assertEqual(temp.getData(), result)

    def test_multiply(self):
        # make sure we can multiply
        temp = self.a*self.b
        result = "10181838148727975708503062096"
        self.assertEqual(temp.getData(), result)
    def test_divide(self):
        # make sure we can multiply
        temp = self.a/self.b
        result = "969231552"
        self.assertEqual(temp.getData(), result)
    def test_modulus(self):
        # make sure we can multiply
        temp = self.a%self.b
        result = "3021441296"
        self.assertEqual(temp.getData(), result)
    def test_greater(self):
        # make sure we can do greater than
        temp = self.a>self.b
        result = True
        self.assertEqual(temp, result)
    def test_less(self):
        # make sure we can do less than
        temp = self.b<self.a
        result = True
        self.assertEqual(temp, result)
    def test_equal(self):
        # make sure we can do equal to
        temp = self.a==self.b
        result = False
        self.assertEqual(temp, result)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDynamicIntegerOperations)
    unittest.TextTestRunner(verbosity=5).run(suite)