# def func1():
#     print("    Subscribe now    ")

# func2 = func1
# del func1
# func2()

# def funcRet(num):
#     if num == 0:
#         return print 
#     if num == 1 :
#         return sum 
# a = funcRet(0)
# print(a)

# def executor(func):
#     func("Thiw")

# executor(print)

def dec1(func1):
    def nowExec():
        print("Executing now...")
        func1()
        print("Executed")
    return nowExec

@dec1
def who_is_harry():
    print("Harry is a good boy")

# who_is_harry = dec1(who_is_harry)

who_is_harry()