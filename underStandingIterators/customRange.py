'''
Created on Feb 23, 2016

@author: rduvalwa2
'''

class CustomRange:
    '''
    This class is a simple example of a custom range.
    It also illustrates an iterator and init. 
    '''

#    def __init__(self, params):
#        '''
#        Constructor
#        '''

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.curr = 0
        return self

    def __next__(self):  # note __next__
        numb = self.curr
        if self.curr >= self.max:
            raise StopIteration
        self.curr += 1
        return numb
    
    def printRange(self):
        for i in CustomRange(10):
            print(i)        
    
if __name__ == "__main__":
    
    aCustRange = CustomRange(10)
    for i in CustomRange(10):
        print(i)

    CustomRange(10).printRange()
    
    print(aCustRange.__dict__)
    print(dir(aCustRange))
    setattr(aCustRange, 'foobar', 123)
    print(dir(aCustRange))
    print(getattr(aCustRange,'foobar'),aCustRange.foobar)
    print(hasattr(aCustRange, 'foobar'))
    delattr(aCustRange, 'foobar')
    print(hasattr(aCustRange, 'foobar'))