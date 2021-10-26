from functools import lru_cache
import time

# code used in the tutorial

@lru_cache(maxsize=5)
def some_work(n):
    time.sleep(n)
    return n

if __name__ == "__main__":
    print("Now running some work")
    some_work(3)
    some_work(1)
    some_work(6)
    some_work(2)
    print("done... Calling again")
    input("press enter to call again ")
    some_work(3)
    some_work(1)
    some_work(6)
    some_work(2)
    print("called again")



# # cache exercise
# # take user input of how many values he wants to cache
# cacheTimes = int(input("How many values do you want to cache? "))

# @lru_cache(maxsize=cacheTimes)
# # this function waits t num of seconds and returns the string value
# def cacheIt(t):
#     time.sleep(t)
#     return f"Done.. called cacheIT() function with the value {t}\n"

# # main function
# if __name__ == "__main__":
#     # take how many times does the user want to call the function cacheIt()
#     times_call = int(input("enter the no of values you want to input: "))

#     # take the values which will be used for the function call to cacheIt()
#     print("\nEnter Values for the number of calls for  cacheIt() function")

#     # List comprehension for taking input and putting them into list
#     cache_values = [int(input("Enter Value: ")) for i in range(times_call)]

#     print("\n")

#     for cache_value in cache_values:
#         print(cacheIt(cache_value))

#     # print(cacheIt(3))
#     # print(cacheIt(4))
#     # print(cacheIt(3))
