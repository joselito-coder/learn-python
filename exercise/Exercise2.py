# Exercise 2 - Faulty Calculator
# Design a calculator which will correctly solve all the problems except the following ones:
# 45*3 = 555, 56+9 = 77 , 56/6 =4 
# Your program should take operator and the two numbers as input from the user and then return the result

# store the expression which will return faulty answers
wrong_answers_dict = {
    "45*3":"555",
    "56+9":"77",
    "56/6":"4"
}
# store the valid operators
valid_operators = ['+','-','/','*']

user_operator = input("Enter your operator:  Valid Options (+, -, /, *)\n>> ")

# take user input and ask for their numbers
user_num_1 = int(input("Enter First number\n>> "))
user_num_2 = int(input("Enter second number\n>> "))

# store the answers as string by joining the first num with the operator and second num
answers_string = str(user_num_1) + user_operator + str(user_num_2)

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
    