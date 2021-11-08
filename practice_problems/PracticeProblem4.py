'''
Author: Joselito
Date: 8-11-2021
Purpose: For practicing programming
'''


# Problem Statement:-
# A palindrome is a string that, when reversed, is equal to itself. Example of the palindrome includes:

# 676, 616, mom, 100001.
# You have to take a number as an input from the user. You have to find the next palindrome corresponding to that number. Your first input should be the number of test cases and then take all the cases as input from the user.
# Input:
# 3
# 451
# 10
# 2133
# Output:
# Next palindrome for 451 is 454
# Next palindrome for 10 is 11
# Next palindrome for 2311 is 2222


# Practice Problem 4 solution

# function to check if a number is a palindrome or not
def isNumPalindrome(num):
    # String version of the number (useful to compare to it's reverse)
    num_str = str(num)
    # Reversed version of the num string
    num_str_rev = num_str[::-1]
    
    # if the reverse of the string is equal to the string then it's a palindrome
    if num_str == num_str_rev:
        return True

    return False

# This Function is used to get the next palindrome of a number
def nextPalindrome(num):
    # IN case the number passed to this function is a palindrome
    num += 1
    # while the number is not a palindrome keep adding 1 to it until it becomes a palindrome
    while not isNumPalindrome(num) :
        num += 1
    return num

if __name__ == "__main__":
    # input the number of test cases
    test_case_count = int(input("How many test cases do you want?\n"))
    # Initiliaze empty list for storing all the test cases
    test_cases = []

    print("Enter All the test cases")
    for i in range(test_case_count):
        # Add the user input to the test_cases list 
        test_cases.append(int(input()))

    # Print the next palindrome for each of the numbers in the test_cases list
    for test_case in test_cases:
        print(f"The next Palindrome for {test_case} is {nextPalindrome(test_case)}")