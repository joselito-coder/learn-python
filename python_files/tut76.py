f1 = open('misc_files/Harry.txt')

try:
    f = open('misc_files/hello.txt')

except EOFError as e:
    print(e)

except IOError as e :
    print(e)

else:
    print("wow there was no error while opening the file")

finally:
    f1.close()
    # f.close()


print("this is important")
