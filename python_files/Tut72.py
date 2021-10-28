
# Quick quiz problem 1
# #  Fibbonacci sequence using genetator
# def fib(num):
#     first = 0
#     second = 1

#     i = 1
#     # Yield the first number as 1
#     yield 1
#     while i < num:

#         yield first + second 
#         first,second = second,first + second
#         i += 1

# fibgen = fib(10)
# for i in fibgen:
#     print(i)

# Quick quiz problem 2

# def genForever():
#     i = 0
#     while 1:
#         yield i +1
#         i +=1


# Generator function to generate Factorial
# def genNFactorial(n):
#     i = 1
#     fact = 1

#     while i <= n:
#         fact *= i
#         yield fact
#         i +=1


# genos = genNFactorial(3)

# for i in genos:
#     print(i)

# def gen(n):
#     for i in range(n):
#         yield i
# g = gen(3)
# print(g.__next__())
# for i in g:
#     print(i)

h = "harry"
ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())