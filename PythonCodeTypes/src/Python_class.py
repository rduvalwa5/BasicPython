''''
Example of python class
'''
from array import *
from test.test_sys_settrace import raises

class arrayTypes:
    
    '''
    Demonstrates array creation    
    '''
    def createArray(self,theType,inList):
        print("in method")
        '''
        for member in inList:
            type(member)
            if not isinstance(member, type(theType)):
                return TypeError
                break
        '''
        anArray = array(theType,inList) # u is unicode character of size 2 bytes
        for item in anArray:
                print(item)
        return anArray
    
    def createFreeArray(self,theType,inList):
        print("in method")
        anArray = array(theType,inList) # u is unicode character of size 2 bytes
        for item in anArray:
                print(item)
        return anArray
    
if __name__ == '__main__':
#    import arrayTypes
    aa = arrayTypes()
    myList = ['a','b','c']
    myType = 'u'
    ch = array('u',myList)
    print("the list", myList)

