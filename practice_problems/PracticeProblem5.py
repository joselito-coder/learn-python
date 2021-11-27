"""
Author: Joselito
Date: 9-11-2021
Purpose: Practicing and solving problems
"""

# Problem Statement:-
# You are given a list that contains some numbers. You have to print a list of the next palindromes only if the number is greater than 10; otherwise, you will print that number.
# Input:
# [1, 6, 87, 43]
# Output:
# [1, 6, 88, 44]

# Practice Problem5 solution:
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
    # In case the number passed to this function is a palindrome
    num += 1
    # keep adding 1 to it until it becomes a palindrome
    while not isNumPalindrome(num) :
        num += 1

    return num


if __name__ == "__main__":

    # Take user input and populate the list
    print("Please enter The num of elements in the list")
    num_of_ele = int(input())
    user_list = []
    print("Enter the values")
    for i in range(num_of_ele):
        user_list.append(int(input()))

    # init output list
    output_list = []

    # append the next palindrome of each number to output list 
    for user_num in user_list:
        if user_num < 10:
            output_list.append(user_num)
            continue
        output_list.append(nextPalindrome(user_num))

    print(f"\n{output_list}")

