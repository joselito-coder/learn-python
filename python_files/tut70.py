class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithbabu.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    

    @property
    def email(self):
        if self.fname == None or self.fname == None:
            return "Please set email using setter"
        return f"{self.fname}.{self.lname}@codewithbabu.com"

    @email.setter
    def email(self,string):
        names = string.split('@')[0]
        self.fname,self.lname = names.split('.')
    
    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

    def __str__(self):
        return f"Employee({self.fname},{self.lname})"


# prints what type the object is
# print(type(skillf))

# # prints the id of an object
# print(id(skillf))

# # dir  returns us a list of attributes and methods associated with an object 
# print(dir(skillf))

# import inspect
# print(inspect.getmembers(skillf,inspect.ismethod))
# for i,j in inspect.getmembers(skillf):
#     if inspect.ismethod(j):
        # print(i)

import inspect
skillf = Employee('Skill', "F")
def print_all_methods(object):
    """ this function inspects an object and prints the Number of methods, and the methods in that particular object
    usage: print_all_methods(Object)  

    Parameters:
    argument1 (Object) : the object from which you want to print the methods
    """

    method_list = []
    method_num = 0

    for method_name,value in inspect.getmembers(skillf,inspect.ismethod):
        method_num += 1
        method_list.append(method_name)

    if method_num != 0:
        print(f"\nTotal number of methods found are: {method_num}\nThe methods are : { '(),   '.join(method_list)}()\n")
    else:
        print(f"No methods found in the Object: {str(object)}")

print_all_methods(skillf)