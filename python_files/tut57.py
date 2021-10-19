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

    @classmethod 
    def from_dashes(cls,string):
        # long version
        # params = string.split('-')
        # return cls(params[0],params[1],params[2])

        # short Version
        return cls(* string.split('-'))

harry = Employee("Harry", 400, "Instructor")
rohan = Employee("Rohan", 200, "Student")
babu = Employee.from_dashes('babu-420-babu_69')

print(babu.printdetails())
