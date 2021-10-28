
class Employee:
    def __init__(self, name, salary, role):
        self.name = name
        self.role = role
        self.salary = salary

    def printdetails(self):
        return f"\n--------Employee Details-----------\n\nname: {self.name}\nsalary: {self.salary}\nrole: {self.role}\n\n--------End Details---------------\n"

    def __repr__(self):
        return f"Employee({self.name},{self.salary},{self.role})"

    def __str__(self):
        return self.printdetails()

    # def __add__(self,other):
    #     return f"{self.name} and {other.name}"

    def __mul__(self,other):
        return f"{self.salary * other.salary } "

    def __pow__(self,other):
        return f"{self.name} is {other} times powerful "
    
    def __getitem__(self,index):
        return f"You cannot index into {self.__repr__()}"


emp1 = Employee('Harry', 347, 'Programmer')
emp2 = Employee('Rohan', 33, 'Cleaner')
# print(emp1 + emp2)

print(emp1 * emp2)
print(emp1 ** 100)
print(emp1[3])

