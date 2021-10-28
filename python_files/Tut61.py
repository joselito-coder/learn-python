class Employee:
    no_of_leaves = 8
    var = 8

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

class Player:
    no_of_games = 4
    var = 9 
    def __init__(self,name,game):
        self.name = name
        self.game = game

    def printdetails(self):
        return f"\n--------Player Details-----------\n\nname: {self.name}\ngame: {self.game}\n\n--------End Details---------------\n"

    @staticmethod
    def printPappu():
        print("This is pappu")
        
        
class CoolProgrammer(Player,Employee):
    language = "C++"
    # var = 10

    def printlanguage(self):
        print(self.language)


harry = Employee("Harry", 400, "Instructor")
rohan = Employee("Rohan", 200, "Student")

subham  = Player("Subham", ["Cricket"])
karan = CoolProgrammer('Karan',"cricket")

# print(karan.printdetails())
# karan.printlanguage()

print(karan.var)