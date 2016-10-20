'''
    ars are argument
    kwargs are key work arguments
    This example demonstrates making a class callable by defining __call__
    this example also demonstrates how to get a class to show its name using __class__ or type()
'''
class funclike:
    def __call__(self, *args, **kwargs):
        print("Args are:", args)
        print("Kwargs are:", kwargs)

class nonfunc:
    def init(self,*args,**kwargs):
        print("Args are:", args)
        print("Kwargs are:", kwargs)
        
        
if __name__ == '__main__':
    f = funclike()
    f(1, 2, 3, this="one", that="the other")
    f(this="one", that="the other")
    nf = nonfunc()
    print(nf.__class__)
    print(type(nf))
    try:
        nf(1, 2, 3, this="one", that="the other")
    except  TypeError:
        print('TypeError: ', nf.__class__ , ' object is not callable')
    
    try:
        nf(this="one", that="the other")
    except TypeError:
        print('TypeError: ',type(nf), ' object is not callable')
    