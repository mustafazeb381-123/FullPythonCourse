#instance & classs variables
class Employees:
    no_of_leaves = 9
    pass

Shahid = Employees()
Hammad = Employees()

Hammad.name = "Hammad"
Hammad.Job = "student"
Hammad.Dept = "CS"

Shahid.name = "shahid iqbal"
Shahid.Job = "Employee"
Shahid.dept = "IT"
print(Employees.no_of_leaves)
print(Shahid.__dict__)
Shahid.no_of_leaves = 10
print(Employees.no_of_leaves)
print(Shahid.no_of_leaves)
print(Shahid.__dict__)
print(Employees.__dict__)
