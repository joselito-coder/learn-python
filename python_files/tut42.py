import time

# initial = time.time()

# k = 0 
# while k < 45:
#     print("This is harry bhai")
#     k += 1
# while_loop_time = time.time() - initial


# initial2 = time.time()

# for i in range(45):
#     print("This is harry bhai")

# for_loop_time = time.time() - initial2

# print( f" while Loop ran in {while_loop_time} seconds " )
# print( f" for Loop ran in {for_loop_time} seconds " )

localtime = time.asctime(time.localtime(time.time()))
print(localtime)