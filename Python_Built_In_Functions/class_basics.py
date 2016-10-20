'''
Created on Mar 4, 2016

@author: rduvalwa2
'''

class MyClassMethod(object):
    '''
    classdocs
    '''

    def __init__(self, obj):
        '''
        Constructor
        '''
        self.theObj = obj
        
    def returnType(self):
        self.myType = type(self.theObj)
        return  self.myType
    
    def thisType(self,i):
        return  type(i)
    
    def get_dict(self):
        
        try:
            return self.theObj.__dict__
        except AttributeError:
            print("Object attribute error")
    
    
    def get_dir(self):
        try:
            return dir(self.theObj)
        except AttributeError:
            print("Object attribute error")

class property_example:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

#    x = property(getx, setx, delx, "I'm the 'x' property.")



    
if __name__ == "__main__":
    from string_related import str_example

    
    aString = "This is string!"
    
    myClassMethod = MyClassMethod(aString)
    x = 'a'.isalpha()
    y = 'a'.isdigit()
    zz = str_example("sas")
    print(myClassMethod.returnType())
    print(myClassMethod.thisType(myClassMethod))
    print(x, type(x), myClassMethod.thisType(x))
    print(y, type(y), myClassMethod.thisType(y))
    print(zz.my_reverse, myClassMethod.thisType(zz))
    stringClassMethod = MyClassMethod(zz)
    print(stringClassMethod.get_dict())
    print(myClassMethod.get_dict())
    print(stringClassMethod.returnType()," : \n",stringClassMethod.get_dir())
    print(myClassMethod.returnType()," : \n", myClassMethod.get_dir())