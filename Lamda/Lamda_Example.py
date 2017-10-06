'''
Created on Oct 5
lambda examples of in line code
@author: rduvalwa2
'''

if __name__ == '__main__':
    
    a = ['a','b','c','d','e']
    b = [1,2,3,4,5]
    
    example = lambda a, b : a + b
    concatArray = lambda a,b: a + b 
    print("example add is ", example(3,4))
    print('concat Array',concatArray(a,b))
    X = [1,2,3,4,5,6]
#    result = lambda a,b: a - b
    
    ZZ = lambda a,b: set(a) - set(b)
    print(set(X) - set(b))
    print(ZZ(X,a))

    