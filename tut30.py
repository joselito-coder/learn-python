f = open("misc_files/Harry.txt")
# print(f.tell())
print(f.readline())
# print(f.tell())
f.seek(11)
print(f.readline())

f.close()