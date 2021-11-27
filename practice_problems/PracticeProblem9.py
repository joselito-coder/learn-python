"""
It's result day at school and not everyone is happy. You decided to make your friends laugh by jumbling their names to come up with some funny names.
Your program should take the number of names and the names separated by space as input. Output should be funny names in the same order.
Input:
Enter number of friends:
3
Enter the name of your 3 friends:
Rohan Das
Shubham Agarwal
Ritesh Arora

Output:
Ritesh Das
Shubham Arora
Rohan Agarwal
"""

"""
Author: Joselito
Date: 13-11-2021
Purpose: Program for funny names
"""

import random

def jumbleNames(names_arr):

    first_names =[]
    last_names = []
    
    # Loop for checking if there are any names without surname or with more than one surname
    for i in range(len(names_arr)):
        full_name = names_arr[i]

        first_names.append(full_name[0])

        # Replace the person with no surname with other person's surname
        if len(full_name) < 2:
            try:
                last_names.append(names_arr[i+1][1])
            except IndexError:
                last_names.append(names_arr[i-1][1])
        # join the surname which has more than 1 words
        elif len(full_name) > 2:
            last_names.append(' '.join(full_name[1:]))
        else:
            last_names.append(full_name[1])

    n = len(first_names)

    # Randomly shuffle the last names
    random.shuffle(last_names)

    # Create an array of randomly shuffled names
    names = [' '.join([first_names[i],last_names[i]]) for i in range(n) ]

    return names


if __name__ == "__main__":
    try:
        num_of_friends = int(input("Enter number of friends: \n"))
    except ValueError:
        print("Please Enter a numeric value")
        exit()

    friends = []

    print(f"Print the name of your {num_of_friends} friends")
    for i in range(num_of_friends):
        friends.append(input().split())

    print()

    for names in jumbleNames(friends):
        print(names)

