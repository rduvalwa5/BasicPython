'''
Created on Mar 4, 2016

@author: rduvalwa2
'''

class property_example:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    
if __name__ == "__main__":
    
    myProp = property_example()
    print(dir(myProp))
    print(myProp.__dict__)
    myProp.setx("fuck this")
    print(myProp.getx())
    print(dir(myProp))
    print(myProp.__dict__)
    myProp.delx()
 
    print("del ", dir(myProp))
    print(myProp.__dict__)
    try:
        print(myProp.getx())
    except AttributeError: 
        print("property_example object has no attribute _x")
    