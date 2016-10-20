'''
Created on Mar 20, 2016
1) Demonstrates unit test class
@author: rduvalwa2
'''
import unittest
from UnitTest_Combined_With_Class import Bunch

class Test(unittest.TestCase):
    def testBunch(self):
        b = Bunch(name="Python 3", language="Python 3.0.1")
        self.assertEqual("Python 3", b.name)
        self.assertEqual("Python 3.0.1", b.language)

if __name__ == "__main__":
    unittest.main()