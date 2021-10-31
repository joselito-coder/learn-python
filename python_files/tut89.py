# a = input("What is your name: ")
# b = input("How much do you earn? ")

# if int(b) ==0 :
#     raise ZeroDivisionError("b is 0 so stopping the program")
# if a.isnumeric():
#     raise Exception("Numbers are not allowed")

# print(f"Hello {a}")

c = input("enter your name : ")

try :
    print(a)
except Exception as e:
    if c == "harry":
        raise ValueError("harry is blocked he is not allowed")
    print("Exception handled")

# Task - Write about 2 built in exception

# 1. ModuleNotFoundError --> yeah Exception tabh raise hoti jab hum koi  module jo maujud nahi  hai woh import kare

# 2. TabError --> yeah Exception tab raise hoti hai jab hum tabs ya phir spaces sahi se nahi dete