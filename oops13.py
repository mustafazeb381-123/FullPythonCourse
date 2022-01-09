#Daimond problem
class A:
    def met(self):
        print("this is method from class A")

class B(A):
    def met(self):
         print("this is method from class B")
class C(A):
    pass
    # def met(self):
    #     print("this is method from class C")

class D(C, B):
    pass
    # def met(self):
    #     print("this is method from class D")

a = A()
b = B()
c = C()
d = D()
d.met()