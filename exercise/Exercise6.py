# Snake water gun
import random

def take_user_input():
    print("\nEnter your choice, valid choices are :")
    print("snake (type s)\nwater (type w)\ngun (type g)")
    try:
        user_choice = input(">> ")

        if user_choice[0].lower() == "s":
            return "snake"
        elif user_choice[0].lower() == "w":
            return "water"
        elif user_choice[0].lower() == "g" :
            return "gun"
        else:
            return None

    except :
        print("Invalid")
        exit()

choices = ['snake','water','gun']
i = 0
user_wins = 0 
computer_wins = 0 

while ( i < 10 ):
    print(f"Round: {i+1}")
    user_input = take_user_input()
    computer_input = random.choice(choices) 

    if user_input not in choices:
        print("Invalid")
        exit()

    print(f"\nThe user choses {user_input}")
    print(f"The computer choses {computer_input}\n")
    
    # user winning conditions
    if user_input == "snake" and computer_input == "water" or user_input == "gun" and computer_input == "snake" or user_input == "water" and computer_input == "gun"   :
        print("The User wins This round\n")
        user_wins += 1
    # draw condition
    elif user_input == computer_input:
        print("Tie\n")
    # else the  computer wins
    else:
        print("Computer wins This Round \n")
        computer_wins += 1

    i += 1

# Print who has won the game
if user_wins > computer_wins:
    print("\n[---- The user has won this game ----]\n")
elif user_wins == computer_wins:
    print("This game is tied")
else:
    print("\n[---- Computer has won the game ----]\n")
