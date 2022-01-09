#Setter and property decoration
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


shahid_iqbal = Employee("shahid", "iqbal")
hammad_ahmad = Employee("hammad", "ahmad")
# print(shahid_iqbal.email)
# shahid_iqbal.fname = "Alama"
shahid_iqbal.email = "Alama.hammad@gmail.com"
print(shahid_iqbal.email)
print(shahid_iqbal.fname)
print(shahid_iqbal.lname)
del shahid_iqbal.email
print(shahid_iqbal.email)