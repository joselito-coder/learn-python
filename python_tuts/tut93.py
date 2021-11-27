# import argparse
# import sys


# def calc(args):
#     operation = args.o
#     x = args.x
#     y = args.y

#     if operation == 'add':
#         return x + y
#     elif operation == 'sub':
#         return x - y
#     elif operation == 'mul':
#         return x * y
#     elif operation == 'div':
#         return x / y
#     else:
#         return "something went wrong"

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()

#     parser.add_argument(
#         '--x', type=float, help='Enter first number. This is an utility for calculation', default=1.1)
#     parser.add_argument(
#         '--y', type=float, help='Enter second number. This is an utility for calculation', default=3.2)
#     parser.add_argument(
#         '--o', type=str, help='Enter operation. This is a utility for babu', default='add')

#     args = parser.parse_args()

#     sys.stdout.write(f"{calc(args)}\n")


# Exercise solution
import argparse

# store the expression which will return faulty answers
wrong_answers_dict = {
    "45*3":"555",
    "56+9":"77",
    "56/6":"4"
}

# Create a parser
parser = argparse.ArgumentParser()

# Add arguments to the parser
parser.add_argument('--fnum',type=int,help='This is the first number',default=45)
parser.add_argument('--snum',type=int,help='This is the second number',default=3)
parser.add_argument('--op',type=str,help='This is the operator\nthe valid operators are:\n-, +, /, * ',default='*')

# parse the arguments
args = parser.parse_args()

# store the valid operators
valid_operators = ['+','-','/','*']

# Operators which the user has chosen
user_operator = args.op

# user supplied numbers
user_num_1 = args.fnum
user_num_2 = args.snum

# store the answers as string by joining the first num with the operator and second num
answers_string = f"{user_num_1}{user_operator}{user_num_2}"

# Check if the user has entered a invalid operator
if user_operator not in valid_operators:
    print("Invalid operator")
# check if the user wants the answers to the questions given in problem statement
elif answers_string in wrong_answers_dict.keys():
    print(wrong_answers_dict.get(answers_string))
# else print the correct answer 
else:
    if user_operator == "*":
        print(user_num_1 * user_num_2)
    elif user_operator == "/":
        print(user_num_1 / user_num_2)
    elif user_operator == "+":
        print(user_num_1 + user_num_2)
    elif user_operator == "-":
        print(user_num_1 - user_num_2)
    else:
        print("Some error occurred")
    