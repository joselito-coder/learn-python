# Exercise 3

# initilize the variables
n = 15
no_of_guesses = 9
user_guess = 0

#  Run the game in a while true loop
while True:
    # Check if user out of guesses
    if(no_of_guesses == 0):
        print("Game over!")
        break

    # Print the number of guesses the user has and take input
    print("You have",no_of_guesses,"Guesses left" )
    user_num = int(input("Enter your number: "))
    # increment user guesses and decrement no of gueses left
    no_of_guesses = no_of_guesses - 1
    user_guess = user_guess + 1

    # condition to check if the user has won
    if user_num == n:
        print("\nCongratulations! You have won the game")
        print("You have cracked the game in",user_guess,"guesses")
        break
    # tell the user whether his number is greater or less than the original number
    elif user_num > n :
        print("\n>> Your number is greater\n")
    elif user_num < n:
        print("\n>> Your number is less\n")

