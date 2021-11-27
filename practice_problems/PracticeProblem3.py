# Problem Statement:-
# You visited a restaurant called CodeWithHarry, and the food items in that restaurant are sorted, based on their amount of calories. You have to reserve this list of food items containing calories.
# You have to use the following three methods to reserve a list:
#     Inbuild method of python
#     List name [::-1] slicing trick
#     Swap the first element with the last one and second element with second last one and so on like,
# [6 7 8 34 5] -> [5 34 8 7 6]
# Input:
# Take a list as an input from the user
# [5, 4, 1]
# Output:
# [1, 4, 5]
# [1, 4, 5]
# [1, 4, 5]
# All three methods give the same results!

# Solution
# Created a copy because if we pass the original list it will alter the original list
def inbuilt_reverse_list(user_list):
    # create a copy of the user list
    list_copy = user_list.copy()
    # Reverse using inbuilt methods
    list_copy.reverse()
    return  list_copy

def slice_reverse_list(user_list):
    # Return the reverse slice of the list
    return user_list[::-1]

def swap_reverse_list(user_list):
    # create a copy of the user list
    temp_list  = user_list.copy()

    # Loop through the half of the list
    for i in range(len(user_list) // 2):
        current_index = i
        last_index = (-(i+1))
        # Swap the first and last value in a list
        temp_list[last_index],temp_list[current_index] = temp_list[current_index],temp_list[last_index]

    return temp_list

if __name__ == "__main__":
    print("please enter a space seperated list of values eg. 1 2 3\n")
    user_input = input()
    if " " not in user_input:
        print("please enter a list with space separated values")
        exit()

    user_list  = user_input.split()

    print(inbuilt_reverse_list(user_list))
    print(slice_reverse_list(user_list))
    print(swap_reverse_list(user_list))

