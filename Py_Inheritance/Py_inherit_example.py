'''
Created on Mar 23, 2016
http://www.python-course.eu/python3_inheritance.php
@author: rduvalwa2
'''

class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname

class Employee(Person):

    def __init__(self, first, last, staffnum):
        Person.__init__(self,first, last)
        self.staffnumber = staffnum

    def GetEmployee(self):
        return self.Name() + ", " +  self.staffnumber

if __name__ == '__main__':

    x = Person("Marge", "Simpson")
    y = Employee("Homer", "Simpson", "1007")

    print(x.Name())
    print(y.GetEmployee())