#  Problem Statement:-

# Generate a random integer from a to b. You and your friend have to guess a number between two numbers, a and b. a and b are inputs taken from the user. Your friend is player 1 and plays first. He will have to keep choosing the number, and your program must tell whether the number is greater than the actual number or less than the actual number. Log the number of trials it took your friend to arrive at the number. You play the same game, and then the person with the minimum number of trials wins! Randomly generate a number after taking a and b as input and don’t show that to the user.


"""
Author: Joselito
Date: 10-11-2021
Purpose: Multiplayer Number guess game
"""

# Random Module for generating a random number
import random

# Class player for the player
class Player():
    number_of_tries = 1
    has_completed = False
    # player constuctor
    def __init__(self,player_name,correct_num):
        self.correct_num = correct_num
        self.name = player_name

    def playGame(self):
        # Print the current player and then ask input
        print(f"\n{self.name.capitalize()}: ")
        user_number = int(input("Guess the number\n"))

        # TAke user input until it is not the correct number
        while user_number != self.correct_num:
            self.number_of_tries += 1
            if user_number < self.correct_num:
                print("\nWrong!! guess a greater number again")
            elif user_number > self.correct_num:
                print("\nWrong guess a smaller number again")
            
            user_number = int(input())
        
        self.has_completed = True
        print(f"\nCorrect You took {self.number_of_tries} Trials to guess the number\n")

            
if __name__ == "__main__":  
    # Handle error if the user types something other than an Integer
    try:
        a = int(input("Enter the value of a\n"))
        b = int(input("Enter the value of b\n"))
    except Exception as e:
        print("Please enter an Integer")
        exit()

    # Quit the program if a is less than b
    if b < a:
        print("the B cannot be less than a")
        exit()

    # Guess a number between a and b
    rndly_guessed_num = random.randint(a, b)
    
    print(f"Please guess a Number between {a} and {b}")

    # Create player instances and play the game
    player1 = Player("player1",rndly_guessed_num)

    rndly_guessed_num_p2 = random.randint(a, b) 
    player2 = Player("player2",rndly_guessed_num_p2)

    player1.playGame()
    player2.playGame()

    if player1.has_completed and player2.has_completed:
        if player1.number_of_tries > player2.number_of_tries:
            print(f"{player2.name.capitalize()} Wins!!")
        elif player1.number_of_tries < player2.number_of_tries:
            print(f"{player1.name.capitalize()} Wins!!")
        else:
            print("It's a draw")
    
    print(f"\nThe number for player 1 was {rndly_guessed_num}")
    print(f"The number for player 2 was {rndly_guessed_num_p2}")
