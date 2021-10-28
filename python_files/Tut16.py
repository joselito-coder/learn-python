# list1 = [["Harry",1],["Larry",2],
#          ["Carry",6],["Marie",250]]

# dict1 = dict(list1)
# print(dict1)

# for item in dict1:
#     print(item)

# for item,lolipop in dict1.items():
#     print(item,lolipop)

# quiz
quiz_list = [int,float,"HArry",3,2,6,19,192,591,2]

for item in quiz_list:
    if str(item).isnumeric() and item > 6:
        print(item)