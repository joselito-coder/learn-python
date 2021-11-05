# numbers = ["12", "223", "10", "35"]

# long way of typecasting to numbers
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])

# # short way
# numbers = list(map(lambda x:int(x),numbers))

# numbers[3] = numbers[3] + 5
# print(numbers)

# def square(a):
#     return a ** 2
# num = [2,3,5,6,76,3,3,2]
# sq = list(map(square,num))
# the above is the same as below
# num = [2,3,5,6,76,3,3,2]
# sq = list(map(lambda x: x**2,num))
# print(sq)

# def square(a):
#     return a**2


# def cube(a):
#     return a ** 3

# func = [square,cube]
# for i in range(5):
#     val = list(map(lambda x : x(i),func))
#     print(val)

# -----------------------------FILTER--------------------------
# list_1 = [1,2,3,4,5,6,7,8,9]

# def is_greater_5(num):
#     return num > 5

# gr_than_5 = list(filter(is_greater_5,list_1))
# print(gr_than_5)
# # -----------------------------REDUCE--------------------------
from functools import reduce

list1 = [1,2,3,4,5]
# short way
num = reduce(lambda x,y: x+y,list1)

#  Long way
# num = 0 
# for i in list1:
#     num = num + i

print(num)
