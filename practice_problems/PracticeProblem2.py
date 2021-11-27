# Problem Statement:-
# Harry Potter has got the “n” number of apples. Harry has some students among whom he wants to distribute the apples. These “n” number of apples is provided to harry by his friends, and he can request for few more or a few less apples.
# You need to print whether a number is in range mn to mx, is a divisor of “n” or not.
# Input:
# Take input n, mn, and mx from the user.
# Output:
# Print whether the numbers between mn and mx are divisors of “n” or not. If mn=mx, show that this is not a range, and mn is equal to mx. Show the result for that number.
# Example:
# If n is 20 and mn=2 and mx=5
# 2 is a divisor of20
# 3 is not a divisor of 20
# …
# 5 is a divisor of 20

# Solution
try:
    # Take number of n
    n = int(input("Please enter the number of apple Harry has\n>> "))

    # Take range input
    print("Enter a range (minimum maximum) ")
    mn = int(input("Min >> "))
    mx = int(input("Max >> "))
except ValueError:
    print("Invalid Input")
    exit()

# Error checking if mn == mx
if mn == mx:
    print("This is not a valid range as minimum number is equal to maximum number")
    exit()

# For loop to determine if a number is divisor of n
for num in range(mn,mx+1):
    if num % n == 0:
        print(f"{num} is a divisor of {n}")
    else:
        print(f"{num} is not a divisor of {n}")