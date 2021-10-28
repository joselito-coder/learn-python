class Employee:
    no_of_leaves = 8

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

class Programmer(Employee):
    no_of_holidays = 56
    def __init__(self, name, salary, role,languages):
        # bad practice
        self.name = name
        self.role = role
        self.salary = salary
        self.languages = languages

    def printprog(self):
        return f"\n--------Programmer Details-----------\n\nname: {self.name}\nsalary: {self.salary}\nrole: {self.role}\nLanguages known: {self.languages}\n\n--------End Details-----------------\n"

        

harry = Employee("Harry", 400, "Instructor")
rohan = Employee("Rohan", 200, "Student")

kausal = Programmer("kaushal",20,"Programmer",["python"])

kausal.printgood("This is berry good")
print(kausal.printprog())
print(kausal.no_of_holidays)