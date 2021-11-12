""" 
Problem Statement
Rohan das is a fraud by nature. Rohan Das wrote a python function to print a multiplication table of a given number and put one of the values (randomly generated) as wrong.
Rohan Das did this to fool his classmates and make them commit a mistake in a test. You cannot tolerate this!
So you decided to use your python skills to counter Rohan’s actions by writing a python program that validates Rohan’s multiplication table.
Your function should be able to find out the wrong values in Rohan’s table and expose Rohan Das as a fraud.
Note: Rohan’s function returns a list of numbers like this
Rohan Das’s Function Input:
rohanMultiplication(6)
Rohan’s function returns this output:
[6, 12, 18, 26, …., 60]
You have to write a function isCorrect(table, number) and return the index where rohan’s function is wrong and print it to the screen! If the table is correct, your function returns None
"""

"""
Author: Joselito
Date: 12-11-2021
Purpose: Expose Rohan Das as a fraud
"""

import random

def rohanMultiplication(number):
    """\nThis is a function created by the one and only henious Rohan Das to trick his classmates into giving a wrong answer in exam, it returns a list of multiplication values which are in order
    """

    # Init mult table list and a random index
    mult_table = []
    rand_index = random.randint(0, 9)

    # Create original table
    for i in range(1,11):
        mult_table.append(number * i)

    # Modify the table randomly
    mult_table[rand_index] = mult_table[rand_index] + random.randint(1, 9)
    
    return mult_table

def isCorrect(table,number):
    """\nThis is a function created by me (Ofcouse) to prevent Rohan Das from tricking his classmates into giving a wrong answer in exam, it validates whether the multiplication in a list is correct or not, If the table is invalid it returns the index where the table is invalid else it returns None
    """
    for index,mult_result in enumerate(table):
        # Store the real result 
        real_result = (index+1) * number
        # return the index if any fake number in  table is found
        if real_result != mult_result:
            return index
        

if __name__ == "__main__":
    # generate multiplication table
    rohan_table = rohanMultiplication(5)
    # Check the table
    print(isCorrect(rohan_table, 5))
