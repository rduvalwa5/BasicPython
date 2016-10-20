'''
Created on Mar 23, 2016
Demostrates Unit Test Setup and implementation

@author: rduvalwa2
'''
import unittest
from car_extended import new_car


class Test(unittest.TestCase):

    def setUp(self):
            self.myCar = new_car('Red','Autin Healey')

    def testCarAttributes(self):
            self.assertEqual('Red',self.myCar.getColor(), "Wrong color")
            self.assertEqual('Autin Healey',self.myCar.getMake(), "Wrong make")
            
    def testSetModelAttribute(self):
        self.myCar.setModel('100-6')
        self.assertEqual(self.myCar.getModel(), '100-6','wrong model')

    def testTopSpeed(self):
        self.myCar.setTopSpeed(150)
        self.assertEqual(self.myCar.get_top_speed(),150, 'wrong top speed')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()