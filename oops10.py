#Public
#protected variables can start from e.g (_protec etc)single underscore
#private variable can start from e.g (__private etc)double underscore
class Employees:
    no_of_leaves = 9
    _protec = 8
    __pr = 50
    def __init__(self, aname, asalary, ajob):#constructor
        self.name = aname#instance
        self.salary = asalary
        self.Job = ajob
    def printdetail(self):
        return f"Name is {self.name}, salary is {self.salary}, Job is {self.Job}"
    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        # param = string.split("-")
        # print(param)
        # return cls(param[0], param[1], param[2])
        return cls(*string.split("-"))
    @staticmethod
    def printgood(string):
        print("this is good " + string)
Shahid = Employees("shahid", 5555, "programmer")
print(Shahid._protec)
print(Shahid._Employees__pr)# the private can use as underscore main class in the print fuction before private method