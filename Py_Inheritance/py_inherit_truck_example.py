'''
Created on Mar 23, 2016

@author: rduvalwa2
'''

class car(object):
    '''
    classdocs
    '''

    def __init__(self,color,make):
        '''
        Constructor
        '''
        self._color = color
        self._make = make
        self._model = None
        
    def getMake(self):
        return  self._make
    
    def setModel(self,mod):
        self._model = mod
        
    def getModel(self):
        if self._model == None:
            return  'model not set'
        else:
            return self._model
        
    def getColor(self):
        return self._color
    

class truck(car):
        def __init__(self, color,make,size):
            car.__init__(self,color, make)
            self._size = size
            self._owner = 'dealer'
            self._status = 'not sold'

        def _get_truck_size(self):
            return  self._size

        def _set_Owner(self,owner):
            self._owner = owner
            
        def _set_status(self,status):
            self._status = status
            
        def _get_status(self):
            return  self._status
        
        def _get_owner(self):
            return self._owner

if __name__ == '__main__':
    
    truck_1 = truck('black','Ford','half ton')
    truck_1.setModel('F150')
    print(truck_1.__dict__)
    print(truck_1.__dir__())
    print('truck_1', truck_1.getMake(), truck_1.getModel(), truck_1.getColor(),truck_1._get_owner(),truck_1._get_status())
    