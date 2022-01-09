#Super, overridding
class A:
    classvar1 = "I am a class variable class A"
    def __init__(self):
        self.var1 = "I am inside class A constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "special"
class B(A):
    classvar1 = "I am in class B"
    def __init__(self):
        # super().__init__()
        self.var1 = "i m inside class B construtor"
        self.classvar1 = "Instance var in class B"
        super().__init__()
        print(super().classvar1)

a = A()
b = B()
print(b.classvar1, b.var1, b.special)