class Employees:
    no_of_leaves = 9
    def __init__(self, aname, asalary, ajob):#constructor
        self.name = aname#instance
        self.salary = asalary
        self.Job = ajob

    def printdetail(self):
        return f"Name is {self.name}, salary is {self.salary}, Job is {self.Job}"

Shahid = Employees("Shahid", 5000, "developer")# class have argument and which is pass to contructor
# Hammad = Employees()
#
# Hammad.name = "Hammad"
# Hammad.salary = 4500
# Hammad.Job = "student"
# Hammad.Dept = "CS"
#
# Shahid.name = "shahid iqbal"
# Shahid.Job = "developer"
# Shahid.salary = 5000
# Shahid.rollno = 13
print(Shahid.name)