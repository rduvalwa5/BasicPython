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

if __name__ == '__main__':
    
    myCar = car('Red','MG')
    myCar.setModel('B')
    print(myCar.__dict__)
    print(myCar.__dir__())
    print('My car ', myCar.getMake(), myCar.getModel(), myCar.getColor())
    