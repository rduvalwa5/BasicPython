'''
Created on Feb 25, 2016

@author: rduvalwa2
'''

class test:
    def __bool__(self):
        return False

def bytearray_example(bar):
    '''
    Return a new array of bytes. The bytearray class is a mutable sequence of integers in the range 0 <= x < 256. 
    It has most of the usual methods of mutable sequences, described in Mutable Sequence Types, as well as most methods 
    that the bytes type has, see Bytes and Bytearray Operations.
    '''
    values = bytearray(elements)
    values[0] = 222
    values[1] = 111
    for value in values:
        yield(value)

def bytes_example(byts, encod):
    '''
    Return a new “bytes” object, which is an immutable sequence of integers in the range 0 <= x < 256. 
    bytes is an immutable version of bytearray – it has the same non-mutating methods and the same indexing 
    and slicing behavior.
    '''
    
def abs_example(inp):
    """
    Return the absolute value of a number. The argument may be an integer or a floating point number. 
    If the argument is a complex number, its magnitude is returned.
    """
    return abs(inp)
    
def all_example(lst):
    '''
    Return True if all elements of the iterable are true (or if the iterable is empty)
    '''
    return  all( type(i) is int for i in lst )

def any_example(lst):
    '''
    Return True if any element of the iterable is true. If the iterable is empty, return False. 
    '''
    return  any( type(i) is int for i in lst )

def ascii_example(c):
    """
    As repr(), return a string containing a printable representation of an object, 
    but escape the non-ASCII characters in the string returned by repr() using \\x, 
    \\u or \\U escapes. This generates a string similar to that returned by repr() in Python 2.
    """
    return  ascii(c)

def bin_example(num):
    """
    Convert an integer number to a binary string. The result is a valid Python expression. 
    If x is not a Python int object, it has to define an __index__() method that returns an integer.
    """
    return bin(num)


if __name__ == "__main__":
    ints = [13433333333333333.555555555555,0.00000000056, -12345, 12]
    empty = []
    steve = 'steve'
    print(abs_example.__doc__)       
    for i in ints:
            print(abs_example(i))
 
    print(all_example.__doc__)           
    lst = [1,2,3,4,5,6,7,8,9]
    print(lst)
    print(all_example(lst))
    lst.append('steve')
    print(lst)
    print(all_example(lst))

    print(any_example.__doc__)
    alpha_lst = ['a','b','c']
    print(alpha_lst)
    print(any_example(alpha_lst))
    alpha_lst.append(1)  
    print(alpha_lst)     
    print(any_example(alpha_lst))

    print(ascii_example.__doc__)
    print("This is \n an\texample")
    print(ascii_example("This is \n an\texample"))
    
    print(bin_example.__doc__)
    print(bin_example(2))
    print(bin_example(123))

    myInst = test()
    print('1: ',bool(True))
    print('2: ',bool(False))
    print('3: ',bool('fuck'))
    print ('4: ',bool(myInst)) #prints "True"
    print ('5: ',myInst.__bool__()) #prints "False"

    elements = [0, 200, 50, 25, 10, 255]
    new_elements = []
    for i in bytearray_example(elements):
        new_elements.append(i)
    print(new_elements)
    print(elements) 