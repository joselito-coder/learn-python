# Fstrings in python
import math
import time

me = "Joselito"
a1 = 32

# a = "This is %s %s" % (me,a1)
# a = "This is {1} {0}"
# b = a.format(me,a1)
# print(b)

a = f"This is {me} {a1} {math.cos(65)}"

print(a)

