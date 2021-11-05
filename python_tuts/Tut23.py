# a = 60
# b = 9

# c = sum((a,b))
# print(c)

def function1(a,b):
    print("Hello this is function 1",a+b)

def function2(a,b):
    """This function calculates the average of two numbers
        This function doesn't work for 3 numbers """
    average = (a+b)/2
    return average

# function1(23,32)
# v = function2(10, 20)
# print(v)

print(function2.__doc__)