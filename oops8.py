#Multiple inheritence
class Employees:
    var = 9
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

class player:
    no_of_gamnes = 4
    var = 8
    def __init__(self, name, games):
        self.name = name
        self.games = games
    def printdetails(self):
        return f"Player name is {self.name} and games that he played is {self.games}"
class coolprogrammer(Employees, player):
    languages = "C++"
    def printlanguages(self):
        print(self.languages)
Shahid = Employees("Shahid", 5000, "developer")# class have argument and which is pass to contructor
Hammad = Employees("Hammmad", 4500, "javacoder")

Iqbal = coolprogrammer("shahid", 55555, "Ceo")
usama = player("Shahid", ["cricket", "football"])
Iqbal.printlanguages()
print(usama.printdetails())
print(Iqbal.var)