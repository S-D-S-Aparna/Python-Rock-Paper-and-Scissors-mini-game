"""
WorkFlow of Project:
1- Input from user(Rock, Paper, Scissors)
2- Computer choice (Computer will choose randomly not conditionaly)
3- Result print

Cases:
A- Rock
Rock - Rock = tie
Rock - paper = Paper win
Rock - Rock = Rock Win
Rock - scissors = Rock Win

B- Paper
Paper - Paper = tie
Paper - Rock = Paper win
Paper - Scissor = Scissor Win

C- Scissors
Scissors - Scissors = tie
Scissors - Rock = Rock win
Scissors - Paper = Scissors win

"""

import random
item_list = ["rock", "paper", "scissors"]

user_choice = input("Enter your move = Rock, Paper, Scissors: ")
comp_choice = random.choice(item_list)

print(f"user choice = {user_choice}, computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("It's a tie!")

elif user_choice == "rock":
    if comp_choice == "paper":
        print("Computer wins!")
    else:
        print("You win!")

elif user_choice == "paper":
    if comp_choice == "scissors":
        print("Computer wins!")
    else:
        print("You win!")

elif user_choice == "scissors":
    if comp_choice == "rock":
        print("Computer wins!")
    else:
        print("You win!")
