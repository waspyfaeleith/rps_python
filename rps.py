import random

def get_user_choice():
    print("Make your choice - (R)ock, (P)aper, or (S)cissors")
    choice = input().lower()
    return choice

def get_computer_choice():
    options = ['Rock', 'Paper', 'Scissors']
    return random.choice(options)

def get_choice(choice):
    options = {
        "r": "Rock",
        "p": "Paper",
        "s": "Scissors"
    }
    return options[choice]

def is_valid(choice):
    if choice == 'r' or choice == 'p' or choice == 's':
        return True
    else:
        return False

def get_winner(player_1_choice, player_2_choice):
    if player_1_choice == player_2_choice:
        return None
    options = {
        "Rock": "Scissors",
        "Paper": "Rock",
        "Scissors": "Paper"
    }
    if (options[player_1_choice] == player_2_choice):
        return player_1_choice
    else:
        return player_2_choice



print ("Let's play 'Rock, Paper, Scissors")
user_choice = get_user_choice()

while (is_valid(user_choice) == False):
    print("Invalid input")
    user_choice = get_user_choice()

user_choice = get_choice(user_choice)

computer_choice = get_computer_choice()

print("You chose {0} - Computer chose {1}".format(user_choice, computer_choice))

winner = get_winner(user_choice, computer_choice)

if (winner == None):
    print("It's a Draw!")
else:
    print(winner + " wins!")
