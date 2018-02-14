# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        """
        a = fact(1)
        if a == 1 :
            print("fact(1) ok")
        else :
            print("fact(1) failure")
        """
        self_compute(self):
            self.assertEqual(utils.fact(1),1)
            self.assertEqual(utils.fact(5),120)
    def test_roots(self):
        """
        a = roots(1,-2,1)
        if a == 1 :
            print("one root ok")
        else :
            print("one root failure")
        """
        self_compute(self):
            self.assertEqual(utils.roots(1,-2,1),1)
        
    def test_integrate(self):
        """
        a = integrate('x',1,2)
        if a == 1.5 :
            print("integration ok")
        else :
            print("integration failure")
        """
        self_compute(self):
            self.assertEqual(utils.integrate('machin', 0,3),11)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
