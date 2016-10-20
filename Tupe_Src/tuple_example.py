'''
Created on Mar 15, 2016

@author: rduvalwa2
'''

class Tuple_Example(object):
    '''
    tuple([iterable])
    Rather than being a function, tuple is actually an immutable sequence type, 
    as documented in Tuples and Sequence Types — list, tuple, range.
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.myTuple = {}
    
    def print_tup(self):
#        print(self.myTuple)
#        print(type(self.myTuple))
        for item in self.myTuple:
                print(item, type(item))

    def print_all(self):
#        print(self.myTuple)
        print(self.myTuple)

    def addItemToTuple(self,item):
        self.myList = list(self.myTuple)
        try:
            self.myList.append(item)
        except Exception as e:
            z = e
            print(z)
        self.myTuple = tuple(self.myList)    
    
    def getLength(self):
        return  len(self.myTuple)
            
    def getMin(self):
        return min(self.myTuple)

    def getMax(self):
        return  max(self.myTuple)
    
    def getRepeat(self, v):
        return  self.myTuple.count(v)
        
if __name__ == "__main__":
    set1Items = ['Jupiter',"Pluto",1001,('a','amber'),('b','blue'),(2*5),[1,2]]
    set2Items = [1,2,'Venus','Mercury','Mars']
    setInt = [9,5,3,1,2,4,6,7,8,9]
    
    a = Tuple_Example()
    a.print_tup()
    print(a.getLength()) 
    
    for i in set1Items:
        a.addItemToTuple(i)
    a.print_tup()  
    print(a.getLength()) 
        
    for i in set2Items:
        a.addItemToTuple(i)
    a.print_tup() 
    print(a.getLength())
    
    
    b = Tuple_Example()

    for i in setInt:
        b.addItemToTuple(i)
    
    b.print_all()
    print(b.getMin())
    print(b.getMax())
    
    print(b.getRepeat(9))
    print(b.getRepeat(2))   