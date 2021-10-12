f = open("misc_files/Harry.txt",'rt')
# print(f.readline())
# print(f.readline())
# print(f.readline())
print(f.readlines())

# content = f.read()
# print(content)

# for line in f:
#     print(line,end='')

# content  = f.read(344)
# print("1",content)
# content  = f.read(344)
# print("2",content)

f.close()