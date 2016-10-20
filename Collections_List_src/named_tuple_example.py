'''
Created on Mar 19, 2016
collections.namedtuple(typename, field_names, verbose=False, rename=False)
Returns a new tuple subclass named typename. The new subclass is used to create tuple-like objects
that have fields accessible by attribute lookup as well as being indexable and iterable. 
Instances of the subclass also have a helpful docstring (with typename and field_names) and 
a helpful __repr__() method which lists the tuple contents in a name=value format.
'''
from collections import namedtuple



if __name__ == '__main__':
    State = namedtuple('State',['state','capital','majorcity'],verbose=False)
    
    WA = State('Washington','Olympia','Seattle')
    OR = State('Oregon','Eugene','Portland')
    CA = State('California','Sacremento','San Francisco')
    #  ,('OR','Eugene'),('CA','Sacremento')])
    west_coast_states = []
    west_coast_states.append(WA)
    west_coast_states.append(OR)
    west_coast_states.append(CA)
  
    print(dir(west_coast_states))
    print(west_coast_states)
    NV = State('Neveda','Reno','Los Vegas')
    west_coast_states.append(NV)
    for item in west_coast_states:
        print(item.state)
        print(item.capital)
        print(item.majorcity)
    