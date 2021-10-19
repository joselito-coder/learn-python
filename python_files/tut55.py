class Employee:
    no_of_leaves = 8

    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary 
        self.role = role

    def printdetails(self):
        return f"The name is {self.name}. The salary is {self.salary} and  role is {self.role}"

harry = Employee( "Harry",444,"Instructor")
# rohan = Employee()

# harry.name = "Harry"
# harry.salary = 444
# harry.role = "Instructor"

# rohan.name = "Rohan"
# rohan.salary = 44
# rohan.role = "Student"
# print(rohan.printdetails())

print(harry.printdetails())