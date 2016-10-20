'''
Created on Apr 12, 2016
    compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
    
    >>> codeobj = compile('x = 2\nprint "X is", x', 'fakemodule', 'exec')
    >>> exec(codeobj)
    X is 2
@author: rduvalwa2
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

def compile_string(s,objName='newObjc',mode='exec',inherit=False,opt=-1):
        obj = compile(s,objName,mode,dont_inherit=inherit,optimize=opt)
        return obj
    
def exec_object(obj):
        exec(obj)
        
def eval_object(obj):
        eval(obj)


if __name__ == "__main__":
    
    stringClass = py_string()
    
    theString = 'print("my message ")'
    theName = 'objName'
    theMode = 'exec'
    
    st = "my reversed string is this 123"
    xx = stringClass.reverseSimple(st)
    print(xx)
# exec("try: \n \t if sam[0] != 'harry': \n \t\t print('hello',  sam) \nexcept: pass")    
    nextString = "stringClass = py_string()\nst = \"my reversed string is this 123\"\nxx = stringClass.reverseSimple(st)\nprint(xx)"
    
    newObj = compile_string(theString,theName,theMode)
    print(newObj)
    print(newObj.__dir__())
    exec_object(newObj)
    
    nextObj = compile_string(nextString,"nextObject",theMode)
    print("exec output")
    exec_object(nextObj)
    print("eval output")    
    eval_object(nextObj)