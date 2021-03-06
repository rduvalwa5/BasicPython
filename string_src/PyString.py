'''
Created on Mar 24, 2015
@author: rduvalwa2
https://docs.python.org/3/library/string.html?highlight=string#module-string
https://docs.python.org/3/library/stdtypes.html#string-methods

This is how to reverse a string
http://stackoverflow.com/questions/18686860/reverse-a-string-in-python-without-using-reversed-or-1
'''

class py_string:
    def __init__(self,strng = "NoString"):
        self._inString = strng
        
    def reverse(self, text = "NoString"):
        if len(text) <= 1:
            return text
        print("text is ", text[1:] + text[0])
        return self.reverse(text[1:]) + text[0]   
    
    def reverseSimple(self, text): 
        return text[::-1]
    
    def makeUpper(self,text):
        return text.upper()
    
    def makeLower(self, text):
        return text.lower()
    
    def makeCaps(self, text):
        return text.capitalize()
    
    def splitString(self, text, sep):
        return text.split(sep)
    
    def stringJoin(self,itr,seq): #list
        return itr.join(seq)
    
    """
    String.Replace(original string,replacement,max number of replacements 
    """
    def stringReplace(self,text,original,replacement,maxreplace=1):
        return text.replace(original,replacement,maxreplace)
    """
    This method can be used to find the first unique character in a string
    """
    def uniquechar(self,seq):
        msg = "no unique chararcter"
        for i in seq:
            ch = i
            chCount = seq.count(ch)
            if chCount == 1:
                msg = ch
                break
        return msg
    
    def _manage_string(self, expression):
        try:
            return str(eval(expression))
        except SyntaxError:
            raise StringError('Invalid expression.')

class StringError(Exception):
        pass
"""
Following are simple out put but I need to write test for them
"""
    
if __name__ == '__main__':
    
    myString = "New string with punctuation! What do you think? No way."
    
    s1 = py_string()
    
    print(s1._inString)
    print("reverse ", s1.reverse("abcdefg"))
    print("reverse simple  " ,s1.reverseSimple(s1._inString))
    
    s2 = py_string(myString)
    print("s2 in string ", s2._inString)
    print(s2.reverse(myString + "0987654321"))
    print(s2.reverse())
    
    print("double reverse ", s2.reverse(s2.reverseSimple(myString)))
    capString = "one two three four five.  Six seven eight?"
    print(capString)
    
    print("Capitilize",s2.makeCaps(capString))
    print("split", s2.splitString(capString, " "))
    splitString = s2.splitString(capString, " ")
    print("spliotString ", splitString)
    newString = ""
    for word in splitString:
        newString = newString + s2.makeCaps(word) + " "    
    print(newString)
    
    separator = "+"
    seq = ("one","two","three","four")
    print("Join ", s2.stringJoin(separator,seq))
    
    stringR = "one two three four five two.  Six seven eight two?"
    print(s2.stringReplace(stringR,"two","twelve"))
    print(s2.stringReplace(stringR,"two","twelve",2))
    
    testString = "abcdefabcde"
    print("Expect \"f\" Return value is ",s1.uniquechar(testString))        
    testString = "abcdefabcdef"
    print("Return value is ",s1.uniquechar(testString))
    testString = "abcdefabef"
    print("Expect \"c\" Return value is ",s1.uniquechar(testString))