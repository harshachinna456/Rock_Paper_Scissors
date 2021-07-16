import  random


options = ["rock", "paper", "scissors"]
user_wins = 0
computer_wins = 0

while  True:
    user_pick = input("Type Rock/Paper/Scissors or Q to quit : ").lower()
    if user_pick == "q":
        break

    if user_pick not in options:
        print("Please enter valid input!")
        continue

    random_number = random.randint(0, 2)
    # rock : 0, paper : 1, scissors : 2

    computer_pick = options[random_number]
    print("Computer picked {}.".format(computer_pick))
    
    if user_pick == computer_pick:
        print("Both pick the same.")
        user_wins += 0
        computer_wins  += 0
    elif user_pick == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
    elif user_pick == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
    elif user_pick == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
    else:
        print("you lost!")
        computer_wins += 1

print("You won {} times.".format(user_wins))
print("Computer won {} times.".format(computer_wins))
print("Hope you enjoyed the game.")
print("Goodbye!")