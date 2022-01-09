#Single inheritence
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
    @staticmethod
    def printgood(string):
        print("this is good " + string)

class programmer(Employees):
    no_of_holydays = 55
    def __init__(self, aname, asalary, ajob, alanguages):
        self.name = aname
        self.salary = asalary
        self.Job = ajob
        self.Languages = alanguages


    def printprog(self):
        return f"The programmer name is {self.name} salary is {self.salary} Job is {self.Job} and languages is {self.Languages}"

Shahid = Employees("Shahid", 5000, "developer")# class have argument and which is pass to contructor
Hammad = Employees("Hammmad", 4500, "javacoder")

Nouman = programmer("Nouman", 5555, "CEO", ["Java","C++","C"])
Sangeen = programmer("Sangeen", 3000, "developer", ["java", "C#", "C", "Ruby"])
print(Nouman.printprog())
print(Sangeen.no_of_holydays)