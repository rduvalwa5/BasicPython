'''
Created on Feb 19, 2016
https://wiki.python.org/moin/Generators
Generators functions allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop.

'''

import itertools
from itertools import takewhile

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','z']
number = [0,1,2,3,4,5,6,7,8,9]

def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1
        
def genCapitals(x=letters):
    for letter in letters:
        if letter.isalpha():
            yield str.upper(letter)

def genLower(x=letters):
    for letter in letters:
        if letter.isalpha():
            yield str.lower(letter)      

def add_squares(max):
    square = (i*i for i in range(1,max))
    bounded_squares = takewhile(lambda x : x< 100, square)
    total = 0
    for i in bounded_squares:
            total += i
            print("total is ",total)
    return total

def add_read_generator(max):
    """
    Read the output of a generator
    note once the generator is read it is remove
    """
    square = (i*i for i in range(1,max))
    bounded_squares = takewhile(lambda x : x< 100, square)
    for item in bounded_squares:
        print("item: ", item)
        
if __name__ == "__main__":
    comp = 0 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9
    result = sum(firstn(10))
    print(result)
    print(result , comp)
    
    max_number = 100
    addedSquares = add_squares(max_number)
    print("addedSquare: ", addedSquares)
    add_read_generator(max_number)
    
    lets = ['a',1,'b',2,'c',3,'d',4,'e',5,'f',6,'g',7,'h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','z']
    nums = [0,1,2,3,4,5,6,7,8,9]  
    
    asciiChar = {}
    for i in genCapitals(lets):
        asciiChar.__setitem__(i, ord(i))
#        print(i , ord(i))
    print('asciichar len', len(asciiChar))
    print('asciichar \n', asciiChar)
#    print(asciiChar.items())
#    print(asciiChar.keys())
#    print(asciiChar.values())
    
    for x in genLower(lets):
            asciiChar.__setitem__(x, ord(x))

    print('asciichar len', len(asciiChar))            
    print('asciichar \n',asciiChar)           