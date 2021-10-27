# def searcher():
#     import time
#     time.sleep(3)
#     book = "this is me and that not me and I is koder"

#     while True:
#         text = (yield)

#         if text in book:
#             print("Your text was found in book")
#         else:
#             print("Your text was not found")

# search = searcher()
# next(search)
# search.send('this is me')
# input()
# search.send('dat not me')
# input()
# search.send('hello world')
# input()
# search.send("Goodbye world")

# Quick quiz solution

def nameInLetters():
    letterFile = open("letters.txt")
    letterContent = letterFile.read()

    while True:
        text = (yield)
        first_letter = text[0].lower()
        if first_letter in letterContent:
            print(f"Your name was found in letter {first_letter}")
        else:
            print("Your name was not found")


nameSearcher = nameInLetters()
next(nameSearcher)

nameSearcher.send("this")
nameSearcher.send("babu")
nameSearcher.send("babu")
nameSearcher.send("babu")
nameSearcher.close()
