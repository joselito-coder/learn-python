# Exercise
# Port python2 code to python 3 code

# Code snippet of python 2
# def greet(name):
#     print "Hello, {0}!".format(name)
# print "What's your name?"
# name = raw_input()
# greet(name)

# Converted code
def greet(name):
    print("Hello, {0}!".format(name))

print("What is your name?")
name = input()
greet(name)