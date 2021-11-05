
class A:
    def met(self):
        print("I am in class A")

    def __init__(self):
        self.babu = "melfern"
        self.unique  = "A"

class B(A):
    def met(self):
        print("I am in class B")

    def __init__(self):
        self.babu = "babuda"
        self.unique  = "B"

class C(A):
    def met(self):
        print("I am in class C")

    def __init__(self):
        self.babu = "chabuda"
        self.unique  = "C"

class D(B,C):
    pass
    # def met(self):
    #     print("I am in class D")

    def __init__(self):
        self.unique  = "D"
        super().__init__()
        self.babu = "melfern"


a = A()
b = B()
c = C()
d = D()

d.met()
print(d.babu)
print(d.unique)

