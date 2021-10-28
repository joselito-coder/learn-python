# list comprehension

# Long way
# ls = []
# for i in range(100):
#     if i % 3 == 0:
#         ls.append(i)
# print(ls)

# short way (list comprehension)
# ls = [i for i in range(100) if i % 3 ==0]
# print(ls)

# # dictionary comprehension
# dict_comp = {i:f"Item {i}" for i in range(1000) }
# print(dict_comp)


noobdict = [1,1,1,1,1,1,1,1,2,23,2,2,2,2,2,2,2,2,2,4234,2,2,24,2,2,1,3,4,232,3,25,252,2]

# reversing the keys and value using dict comprehension
# dict_comp = {value:key for key,value in dict_comp.items()}
# print(dict_comp)

# set comprehnsion
set_comp = {i for i in noobdict}
print(set_comp)

# generator comprehension
evens = (i for i in range(100) if i%2 ==0)

print(evens.__next__())
for i in evens:
    print(i)

# genComp = (i for i in range(100) if i % 2 ==0)

# for i in genComp:
#     print(i)

# quiz question
# try:
#     item_no = int(input("How many items do you want to input: "))
#     user_list = [input(f'Enter value : ') for i in range(item_no) ]

#     print("\nWhat type of comprehension do you want to make?:")
#     print("Press\n* 1 for list\n* 2 for dict\n* 3 for set\n")
#     user_comp = int(input(">> "))

#     if user_comp == 1:
#         # list comprehension
#         list_comp = [i for i in user_list]
#         print(type(list_comp))
#         print(list_comp)
#     elif user_comp == 2:
#         # Create the dict comp
#         dict_comp = {i:user_list[i] for i in range(len(user_list))}
#         # reversing the key and value
#         dict_comp = {value:key for key,value in dict_comp.items()}
#         # Printing type
#         print(type(dict_comp))
#         # printing the dicts
#         print(dict_comp)
#     elif user_comp ==3 : 
#         set_comp = {i for i in user_list}
#         print(type(set_comp))
#         print(set_comp)
# except Exception as e:
#     print(e)