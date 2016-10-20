'''
Created on Sep 24, 2013

@author: rduvalwa2
'''
"""
Demonstrate magic methods for attribute access.
"""
class AttrMixin:
    "Displays a message when an object's attributes are retrieved or set."    
 
    def __setattr__(self, key, value):
        print("ATTR: setting attribute {0!r} to {1!r}".format(key, value))
        self.__dict__[key] = value
 
    def __getattr__(self, key):
        print("ATTR: getting attribute {0!r}".format(key))
        self.__setattr__(key, "No value")
        return "No value"

    def __delattr__(self, key):
        print("ATTR: Deleting key {0!r}".format(key))
        object.__delattr__(self, key)
        
    def __hasattr__(self,nam):
        print("ATTR: checking attribute {0!r}".format(nam))
        return  hasattr(self,nam)
 
class Person(AttrMixin):
    "Represents a person"
    def __init__(self, name):
        self.name = name
      
if __name__ == "__main__":
#    from attrmagic_edit import *
    steve = Person("Steve Holden")
    steve.newattr = 'U.S. Air Force'
    steve.age = 45
    steve.schools = ['Lincoln','Hamilton','UW']
    print(hasattr(steve, 'age'))
    print(steve.__hasattr__('age'))
    print("newattr  ", steve.newattr)
    print("name ", steve.name)
    print("dict   ", steve.__dict__)
    steve.__delattr__('age')
    print(hasattr(steve, 'age'))
    print("dict   ", steve.__dict__)

"""    
ATTR: setting attribute 'name' to 'Steve Holden'
ATTR: setting attribute 'newattr' to 'U.S. Air Force'
ATTR: setting attribute 'age' to 45
ATTR: setting attribute 'schools' to ['Lincoln', 'Hamilton', 'UW']
True
ATTR: checking attribute 'age'
True
newattr   U.S. Air Force
name  Steve Holden
dict    {'name': 'Steve Holden', 'age': 45, 'schools': ['Lincoln', 'Hamilton', 'UW'], 'newattr': 'U.S. Air Force'}
ATTR: Deleting key 'age'
ATTR: getting attribute 'age'
ATTR: setting attribute 'age' to 'No value'
True
dict    {'name': 'Steve Holden', 'age': 'No value', 'schools': ['Lincoln', 'Hamilton', 'UW'], 'newattr': 'U.S. Air Force'}
"""