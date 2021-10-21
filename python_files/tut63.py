# Public -
# Private -
# Protected -

class Employee:
    no_of_leaves = 8
    var = 8
    public = 0
    _protected = 32
    __private = 10

    def __init__(self, name, salary, role):
        self.name = name
        self.role = role
        self.salary = salary

    def printdetails(self):
        return f"\n--------Employee Details-----------\n\nname: {self.name}\nsalary: {self.salary}\nrole: {self.role}\n\n--------End Details---------------\n"

    @classmethod
    def change_leaves(cls,new_leaves):
        cls.no_of_leaves = new_leaves

    @classmethod 
    def from_dashes(cls,string):
        # long version
        # params = string.split('-')
        # return cls(params[0],params[1],params[2])

        # short Version
        return cls(* string.split('-'))

    @staticmethod 
    def printgood(string):
        print(f"This is good {string}")


# print(Employee.public)
emp = Employee('Babu', 322, "Brogrammer")

print(emp.public)
print(emp._protected)
print(emp._Employee__private)