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

    @classmethod
    def from_dash(cls, string):
        # param = string.split("-")
        # print(param)
        # return cls(param[0], param[1], param[2])
        return cls(*string.split("-"))

Shahid = Employees("Shahid", 5000, "developer")# class have argument and which is pass to contructor
Hammad = Employees("Hammmad", 4500, "javacoder")
Malaika = Employees.from_dash("Malaika-400- students")
print(Malaika.Job)

# Hammad.change_leaves(38)
# Employees.change_leaves(38)
# print(Hammad.no_of_leaves)