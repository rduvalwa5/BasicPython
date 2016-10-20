'''
Created on Mar 23, 2016
Extended uses the super class as import but does not have an init
@author: rduvalwa2
'''

from car_example import car


class new_car(car):

    def setTopSpeed(self, topspeed):
            self._topSpeed = topspeed
#            print(self._topSpeed)
 
    def get_top_speed(self):
            return self._topSpeed
 

if __name__ == '__main__':      
    myCar = new_car('Red','Autin Healey')
    print(myCar.getColor(), myCar.getMake())
    myCar.setModel('100-6')
    myCar.setTopSpeed(120)
    
    print(myCar.__dict__)
    print(myCar.__dir__())
    
    print(myCar.getColor(),myCar.getMake(), myCar.getModel(),myCar.get_top_speed())
        
    '''    
    import unittest
    class TestBunch(unittest.TestCase):
        def test_attributes(self):
            myCar = new_car('Red','Autin Healey')
            print(myCar.getColor())
            self.assertEqual('Red', myCar.getColor())
            self.assertEqual('Ausitn Healey',myCar.getMake())

    unittest.main()
    '''