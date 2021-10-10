grocery = ['Harpik', 'Halls', 'Bhindi', 'Brown bread', 101]
# print(grocery[5])

numbers = [6, 2, 4, 20, 11]
# numbers.sort()
# numbers.reverse()
# print(len(numbers))
# print(max(numbers))
# print(min(numbers))
# numbers = []
# numbers.append(71)
# numbers.append(1)
# numbers.append(91)
# numbers.insert(2, 69)
# numbers.remove(2)
# numbers.pop()
# numbers[1] = 69
# print(numbers)

# Mutable - can change
# Immutable - cannot change
# tp = (1, 2, 3) 
# tp = (1,)# ==> cannot do (1) as it will be stored as integer rather do (1,)
# tp[1] = 8 # will give error
# print(tp)

# Swapping
a = 1
b = 8
# Tradition way
# temp = a
# a = b
# b = temp

# The way of the python
a,b = b,a

print(a,b)