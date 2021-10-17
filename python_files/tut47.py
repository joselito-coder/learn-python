lis = ["John",'cena','Randy',"orton","Shemus","Khali","Jindar Mahal"]

# long method to print [name and ...]
# for i in lis:
#     print(f"{i} and",end=' ')
# print("other wwe superstars")

# join method way
a = ' and '.join(lis)
print(f"{a} and other wwe superstars")