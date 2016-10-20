'''
order is defined by the so-called "Method Resolution Order" or in short MRO.1\
'''
class A:
    def m(self):
        print("m of A called")

class B(A):
    def m(self):
        print("m of B called")
    
class C(A):
    def m(self):
        print("m of C called")

class D(B,C):
    def m(self):
        print("m of D called")
        
if __name__ == '__main__':
#    from super1 import A,B,C,D
    print("fuck")
#    z = B()
#    z.m()
    x = D()
    B.m(x)
    ax = A()
    ax.m()
    D.m(C)
    D.m(A)

    
    '''
    >>> from super1 import A,B,C,D
    >>> x = D()
    >>> B.m(x)
    m of B called
    >>> C.m(x)
    m of C called
    >>> A.m(x)
    m of A called
    '''