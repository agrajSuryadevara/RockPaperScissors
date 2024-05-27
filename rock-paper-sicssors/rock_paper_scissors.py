import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]
#            0        1         2 

while True:
    user_input = input("Type Rock/Paper/Scissors OR q to exit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        print("Invalid input. Please try again.")
        continue

    random_number = random.randint(0, 2)
    #rock = 0
    #paper = 1
    #scissors = 2

    computer_pick = options[random_number]
    print("Computer chose", computer_pick + ".")

    if (user_input == "rock" and computer_pick == "scissors") or \
       (user_input == "paper" and computer_pick == "rock") or \
       (user_input == "scissors" and computer_pick == "paper"):
        print("You Won!")
        user_wins += 1
    
    else: 
        print("You Lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("Computer won", computer_wins, "times.")
print("Thank you for playing!")