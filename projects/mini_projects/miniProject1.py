
# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

# HarryLibrary = Library(listofbooks, library_name)


#dictionary (books-nameofperson)

# create a main function and run an infinite while loop asking
# users for their input

class Library:
    # Dictionary to store borrowed books
    borrowed_books = dict()

    # Constructor
    def __init__(self, listofbooks, library_name):
        self.books = listofbooks
        self.name = library_name

    #  function to display books
    def displayBooks(self):
        # Print books only if there are books avaialble in self.books
        if len(self.books) != 0:
            print("\nThe available books are:\n")
            for index, book in enumerate(self.books):
                print(index+1, book)
            print()
        else:
            print("\nThere are no books available Please add Books")

    def lendBook(self, bookname, username):
        #  Check if the book is available:
        if bookname in self.books:
            self.borrowed_books.update({bookname: username})
            print(f"the book has been issued to {username}")
            book_index = self.books.index(bookname)
            del self.books[book_index]
        #  Handle when the book is already borrowed
        elif bookname in self.borrowed_books.keys():
            print(
                f"The Book has already been borrowed by {self.borrowed_books.get(bookname)}")
        else:
            print(f"the book is not available")

    def addBook(self, bookname):
        if bookname in self.books:
            print("The book is already present")
        else:
            self.books.append(bookname)
            print("The book was added successfully")

    def returnBook(self, bookname):
        if bookname in self.borrowed_books.keys():
            self.books.append(bookname)
            del self.borrowed_books[bookname]
            print("the book has been returned")
        else:
            print("that book is not borrowed")


HarryLibrary = Library(
    ['magi', 'solo leveling', 'fun with git', 'linux fun'], 'babu')


def main():
    print("\nWhat do you want to do?")
    print("(1) for displaying all the books")
    print("(2) for borrowing an available book")
    print("(3) for adding a book")
    print("(4) for returning a book")
    print("(5) for exit\n")

    try:
        user_input = int(input(">> "))
        if user_input == 1:
            HarryLibrary.displayBooks()

        elif user_input == 2:
            username = input("Enter username :  ")
            book_name = input("Enter book name: ")
            HarryLibrary.lendBook(book_name,username)
        elif user_input == 3:
            bookname = input("Enter book name: ")
            HarryLibrary.addBook(bookname)
        elif user_input == 4:
            bookname = input("Enter book name: ")
            HarryLibrary.returnBook(bookname)
        elif user_input == 5:
            exit()
        else:
            print("Please enter a valid input")

    except ValueError:
        print("Please Try again\n")
        main()

if __name__ =="__main__":
    print(f"Welcome to {HarryLibrary.name} Library ")
    while 1:
        main()
