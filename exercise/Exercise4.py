# Exercise 4 solution

# function to print foward pattern
def print_pattern_forward(n):
    for i in range(1,n+1):
        for j in range(i):
            print("*",end='')
        print()
    
# function to Print the backward pattern
def print_pattern_backward(n):
    for i in range(n,0,-1):
        for j in range(i):
            print('*',end='')
        print()

# take user input
n = int(input("Enter any number\n>> "))

# convert to boolean
bool_var = bool(int(input("Choose one of the following:\n0 Or 1\n>> ")))

# Print pattern based on the boolean
if bool_var:
    print_pattern_forward(n)
else:
    print_pattern_backward(n)