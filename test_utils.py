# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
import utils
import doctest

class TestUtils(unittest.TestCase):
    def test_fact(self):
        """
        >>>fact(1)
        1
        >>>fact(5)
        120
        """
        self_fact(self):
            self.assertEqual(utils.fact(1),1)
            self.assertEqual(utils.fact(5),120)
    def test_roots(self):
        """
        >>>roots(1,-2,1)
        1
        """
        self_roots(self):
            self.assertEqual(utils.roots(1,-2,1),1)
        
    def test_integrate(self):
        """
        >>>integrate('machin',0,3)
        11
        """
        self_compute(self):
            self.integrate(utils.integrate('machin', 0,3),11)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
