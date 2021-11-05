# is - reference equality - Two references refer to the same object
# == - value equality - Two objects have the same value

# Example
a = [1,2,3,4]
b = a
b[0] = 99
print(a,b)
print(a is b)
print(a == b)

a = [5,10,15,20,25]
b = a[:]
print(a,b)
print(a is b)
print(a == b)

# Task:
# a =[6, 4 , "34"]
# b = [6, 4 , "34"]
# print(b is a)
# This Will print false