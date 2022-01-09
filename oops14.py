#operator overlodding and Dunder methhod
class Employees:
    no_of_leaves = 9
    def __init__(self, aname, asalary, ajob):#constructor
        self.name = aname#instance
        self.salary = asalary
        self.Job = ajob

    def printdetail(self):
        return f"Name is {self.name}, salary is {self.salary}, Job is {self.Job}"
    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves
    def __add__(self, other):#dunder method which is start from double underscore and also end from double underscore
        return self.salary + other.salary
    def __truediv__(self, other):
        return self.salary / other.salary
    def __mul__(self, other):
        return self.salary * other.salary
    def __repr__(self):
        return f"Employee({self.name}, {self.salary}, {self.Job})"
    def __str__(self):
        return f"Name is {self.name}, salary is {self.salary}, Job is {self.Job}"
emp1 = Employees("shahid", 555, "programmer")
emp2 = Employees("hammad", 4, "cleaner")
# print(emp1 + emp2)
# print(emp1/emp2)
# print(emp1*emp2)
# print(repr(emp1))
print(str(emp1))