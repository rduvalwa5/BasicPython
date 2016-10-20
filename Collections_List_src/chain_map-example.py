'''
Created on Mar 17, 2016

@author: rduvalwa2
'''

from collections import ChainMap

class MychainMap(object):
    '''
    https://docs.python.org/3/library/collections.html#collections.ChainMap
    A ChainMap class is provided for quickly linking a number of mappings so they can be treated 
    as a single unit. It is often much faster than creating a new dictionary and running multiple
    update() calls.
    A ChainMap groups multiple dicts or other mappings together to create a single, updateable 
    view. If no maps are specified, a single empty dictionary is provided so that a new chain 
    always has at least one mapping.  The underlying mappings are stored in a list. 
    That list is public and can accessed or updated using the maps attribute. 
    There is no other state.
    Lookups search the underlying mappings successively until a key is found. 
    In contrast, writes, updates, and deletions only operate on the first mapping.
    '''
    def __init__(self, st,cap):
        '''
        Constructor
        '''
        self._st = st
        self._cap = cap
        
    def combine(self):
        self._comb = ChainMap(self._st,self._cap)
        print(self._comb)
        return  self._comb
    
if __name__ == "__main__":
    states = {'WA':'Washington','OR':'Oregon','CA':'California'}
    capitals = {'Olympia':'WA','Eugene':'OR','Sacremento':'CA'}
    x = MychainMap(states,capitals)
    z = x.combine()
    print(z)
    for c,s in z.items():
        print(c,s)
        
            
    a = {'a': 1, 'b': 2}
    b = {'b': 10, 'c': 11}
    y = MychainMap(a,b)
    zz = y.combine()
    for a, b in zz.items():
        print(a,b)