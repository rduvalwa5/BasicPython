'''
-The Diamand Problem or the ,,deadly diamond of death-
    Diamond Problem The "diamond problem" (sometimes referred to as the "deadly diamond of death") 
    is the generally used term for an ambiguity that arises when two classes B and C inherit 
    from a superclass A, and another class D inherits from both B and C. 
    If there is a method "m" in A that B or C (or even both of them) )has overridden, 
    and furthermore, if does not override this method, 
    then the question is which version of the method does D inherit? 
    It could be the one from A, B or C 
'''

class A:
        def m(self):
            return "m of A called"

class B(A):
        def m(self):
            return "m of B called"
    
class C(A):
        def m(self):
            return "m of C called"

class D(B,C):
        print("Class B has precedence over class C")
        pass

class E(C,B):
        print("Class C has precedence over class B")
        pass

if __name__ == "__main__":
    
    import unittest
    class TestClasses(unittest.TestCase):
            def testclassA(self):
                c = A()
                expected = "m of A called"
                self.assertEqual(expected, c.m())
                   
            def test_class_B(self):
                cls = B()
                expected = "m of B called"
                self.assertEqual(expected, cls.m()) 
 
            def test_class_C(self):
                cls = C()
                expected = "m of C called"
                self.assertEqual(expected, cls.m()) 
 
            def test_class_D(self):
                cls = D()
                expected = "m of B called"
                self.assertEqual(expected, cls.m()) 
                
            def test_class_E(self):
                cls = E()
                expected = "m of C called"
                self.assertEqual(expected, cls.m())                 

    unittest.main()