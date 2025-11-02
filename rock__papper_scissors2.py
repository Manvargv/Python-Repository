"python" #Rock_Paper_Scissors.py
 

from random import randrange 

# Function to get user's choice
def get_user_weapon():
    print("\nchoose your weapon:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choice = int(input("Enter 1, 2, or 3: "))
    return choice

# function to get opponent's choice
def get_opponent_weapon():
    choice = randrange(1, 4) # random number 1 to 3
    return choice

# function to decide the winner 
def determine_winner(user, opponent):
    if user == opponent:
        print("It's a tie!")
    elif user == 1 and opponent == 3:
        print("You win! Rock beats Scissors.")
    elif user == 2 and opponent == 1:
        print("You win! Paper beats Rock.")
    elif user == 3 and opponent == 2:
        print("You win! Scissors beats Paper.")
    else:
        print("You lose!")

# main function to runthe game 
def main():
    play_again = "y"

    while play_again == "y":
        user_choice = get_user_weapon()
        opponent_choice = get_opponent_weapon()

        print("You chose:", user_choice)
        print("Opponent chose:", opponent_choice)

        determine_winner(user_choice, opponent_choice)

        play_again = input("Play again? (y/n): ")

    print("\nCompleted by, Manuel Vargas")

# Run the game 

main()
