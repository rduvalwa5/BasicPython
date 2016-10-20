'''
These are examples of bytes and chars
'''
import string

class  str_example:
    """
    class str(object=b'', encoding='utf-8', errors='strict')
    Return a string version of object. If object is not provided, returns the empty string.
    Otherwise, the behavior of str() depends on whether encoding or errors is given, as follows.
    """
    def __init__(self, strg):
        self.my_string = strg
        self.my_reverse = self.my_string[::-1]
        
    def reverse_example(self):
        return(reversed(self.my_string))
        
    def __str__(self):
        return str(self.my_string)
    
    def __reverse__(self):    
        return self.my_reverse

    def is_char_present(self,c):
        if c in self.my_string:
                return  True
        else:
            return  False

    def what_is_it(self, s):
        for c in s:
            if c.isalpha():
                print (c + ": is alpha")
            elif c.isalnum():
                print (c + ": is numeric")
            elif 'c'.isdecimal():
                print (c + ": is decimal")
            elif c in string.whitespace:
                print (c + ": is white space")        
            elif c in string.punctuation:  # import string
                    print (c + " is punctuation")
            elif c.isprintable():
                print (c + " is printable")
            else:
                print  ("I don't know")
        
if __name__ == "__main__":
    
    print(str_example.__doc__)
    print(str_example.__dict__)
    print(dir(str_example))

    a_str = str_example("fuck this")
    print(a_str.__str__())
    print(a_str.__reverse__())
    print("start reversed")
    for c in a_str.reverse_example():
        print(c)

    print(a_str.is_char_present('c'))
    print(a_str.is_char_present('a'))

    testString = "I don't know 1 from 2 '1.1' ?\n!{}\t[]-+=?!"
    b_str = str_example(testString)
    b_str.what_is_it(b_str.my_reverse)
        