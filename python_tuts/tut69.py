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


babu = Employee('Melfern', 'Babu')

print(babu.explain())
babu.fname = "melfern"
babu.lname = 'babu'
print(babu.email)

babu.email = "hello.world@babu.com"
print(babu.email)

del babu.email
print(babu.email)
print(babu.fname)