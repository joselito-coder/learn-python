l1 = ["Bhindi","chopsticks","Aloo","chowmein"]

# i = 1 
# for item in l1:
#     if i % 2 != 0:
#         print(f"Please buy {item}")
#     i += 1

# Enumerate function

for index,item in enumerate(l1):
    if index % 2 == 0:
        print(f"Please buy {item}")