class Employee:
    no_of_leaves = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.role = role
        self.salary = salary

    def printdetails(self):
        return f"name: {self.name}\nsalary: {self.salary}\nrole: {self.role}"

    @classmethod
    def change_leaves(cls,new_leaves):
        cls.no_of_leaves = new_leaves

harry = Employee("Harry", 400, "Instructor")
rohan = Employee("Rohan", 200, "Student")

harry.change_leaves(20)
print(harry.no_of_leaves)
