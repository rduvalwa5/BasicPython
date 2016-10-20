'''
Created on Mar 22, 2016
Example of extending a class in Python
@author: rduvalwa2
'''

class Color:
    def __init__(self, color):
        self.color = color
    def getcolor(self):
        return self.color
    
class ColorExtend(Color):
    def getcolor(self):
        self.color = 'anything but ' + self.color
        return self.color
    
    
if __name__ == '__main__':
    
    colorBlue = Color("blue")
    print(colorBlue.getcolor())
    notColor = ColorExtend("blue")
    print(notColor.getcolor())
    
