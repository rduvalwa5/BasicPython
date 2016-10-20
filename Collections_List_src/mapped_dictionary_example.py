'''
Created on Mar 15, 2016

@author: rduvalwa2
'''

class map_dictionary:
    def __init__(self):
#        self.t_name = t_name
        self.name = {}
        print(type(self.name))
        
    def add_item(self,element, value):
        self.name[element] = value
        
    def print_tuple(self):
        print(self.name)
        
    def remove_item(self,key):
#        print('key ', key, self.name[key])
        try:
            del self.name[key]
        except KeyError as ex:
            print('KeyError exception',ex)
 
        
if __name__ == "__main__":
    tname = "myTup"
    myTup = map_dictionary()
    
    myTup.add_item('length', 10)
    myTup.add_item('width', 5)
    myTup.add_item('depth', 6)
    print(myTup.name['length'])
    cube = myTup.name['length'] * myTup.name['width'] * myTup.name['depth']
    myTup.add_item('cubed', cube)
    myTup.print_tuple()
    print(dir(myTup))
    print(myTup.__dir__())
    print(myTup.__dict__)
    myTup.remove_item('big')
    myTup.remove_item('length')
    print(myTup.__dict__)