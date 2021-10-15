
def factorial_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac* (i + 1)
    return fac

def factorial_recursive(n):

    if n == 1:
        return 1
    
    else:
        return n * factorial_recursive(n-1)


number = int(input("Enter number: "))
# print("factorial using iterative approach is : ",factorial_iterative(number))
# print("factorial using recursive approach is : ",factorial_recursive(number))

# Quick quiz: write program to print the fibbonaci series

def fibbonaci(n):
    if n == 1:
        return 0
    
    elif n == 2:
        return 1
    else:
        return fibbonaci(n-1) + fibbonaci(n-2)

print(fibbonaci(number))
