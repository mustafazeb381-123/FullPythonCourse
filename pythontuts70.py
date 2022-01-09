#object introspection
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{self.fname}.{self.lname}@gmail.com"
    def explain(self):
        return f"Employee name is {self.fname}{self.lname}"
    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "The Email is not set"
        return f"{self.fname}.{self.lname}@gmail.com"
    @email.setter
    def email(self, string):
        names = ("Setting now......")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]
    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

skillf = Employee("skill", "F")
print(skillf.fname)
print(skillf.lname)
print(skillf.email)
o = "this is string"
print(dir(o))
print(dir(skillf))
print(id("this is so strong"))
print(id("he fuck you"))

import inspect
print(inspect.getmembers(skillf))
