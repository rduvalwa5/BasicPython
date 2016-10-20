'''
These are examples of bytes and chars
'''

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
    Return a new â€œbytesâ€� object, which is an immutable sequence of integers in the range 0 <= x < 256. 
    bytes is an immutable version of bytearray â€“ it has the same non-mutating methods and the same indexing 
    and slicing behavior.
    '''
    

def chr_example(ch):
    '''
    chr(i)
    Return the string representing a character whose Unicode code point is the integer i. 
    For example, chr(97) returns the string 'a', while chr(957) returns the string 'Î½'. This is the inverse of ord().
    The valid range for the argument is from 0 through 1,114,111 (0x10FFFF in base 16). 
    ValueError will be raised if i is outside that range.
    '''
    try:
        ret = chr(ch)
        return ret
    except  ValueError as v:
        print(v)
        return  'Out of valid range 0 to 1,114,111'

def ord_example(ch):
    """
    Given a string representing one Unicode character, return an integer representing the Unicode code 
    point of that character. 
    For example, ord('a') returns the integer 97 and ord('ν') returns 957. This is the inverse of chr().
    """
    try:
        return ord(ch)
    except TypeError as v:
#        print(v)
        return('ch is: ', v)

if __name__ == "__main__":

    print(bytearray_example.__doc__)
    elements = [0, 200, 50, 25, 10, 255]
    new_elements = []
    for i in bytearray_example(elements):
        new_elements.append(i)
    print(new_elements)
    print(elements) 
    
    print(bytes_example.__doc__)
    
    
    print(chr_example.__doc__)
    print(chr_example(0))
    print(chr_example(1114111))
    printable = []
    for c in range(32,600):
        printable.append((c , chr_example(c)))
#    print(chr_example(1114112))
    keyboard =[]
    for c in range(32,127):
        keyboard.append(chr(c))

    print(keyboard)    
    for alpha in keyboard:
#        if (alpha % 2 == 0):
            print(alpha, ord_example(alpha))
        
    print('\\n is ',ord_example('\n'))
    print(ord_example('ab'))
    print(ord_example.__doc__)