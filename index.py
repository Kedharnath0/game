# Developed by Ch.Kedhar Nath and P.Bhanu Tej.
import random
c=0
b=0
print('Note : Skip to stop the game.\n')
choice = ['rock','paper','scissor']
game_type=input("Enter game type(pvc or pvp): ")
if game_type == "pvc":
    while True:
        Your_choice = input("Enter your choice: ")
        if Your_choice == "":
            print("\n\tYour Points:", b)
            print("\tComputer's Points:", c)
            break
        elif Your_choice not in choice:
            print('Invalid Entry')
            while Your_choice in choice:
                Your_choice = input("Enter your choice: ")
        else:
            print("Your Choice:", Your_choice)
            Computer_choice = random.choice(choice)
            print("Computer's Choice:", Computer_choice)
            if Your_choice == "rock" and Computer_choice == "paper":
                result = "You Lose!"
                print("Result:", result)
                c = c + 1
            elif Your_choice == "paper" and Computer_choice == "scissor":
                result = "You Lose!"
                print("Result:", result)
                c = c + 1
            elif Your_choice == "scissor" and Computer_choice == "rock":
                result = "You Lose!"
                print("Result:", result)
                c = c + 1
            elif Your_choice == Computer_choice:
                result = "Draw"
                print("Result:", result)
            else:
                result = "You Win!"
                print("Result:", result)
                b = b + 1

elif game_type == "pvp":
    while True:
        p1_choice = input("Enter player 1 choice: ")
        p2_choice = input("Enter player 2 choice: ")
        if p1_choice == "" or p2_choice == "":
            print("\n\tPlayer 1's Points:", b)
            print("\tplayer 2's Points:", c)
            break
        elif p1_choice not in choice:
            print('Invalid Entry')
            while p1_choice in choice:
                p1_choice = input("Enter player 1 choice: ")
        elif p2_choice not in choice:
            print('Invalid Entry')
            while p2_choice in choice:
                p2_choice = input("Enter player 2 choice: ")
        else:
            print("Player 1's Choice:", p1_choice)
            print("player 2's Choice:", p2_choice)
            if p1_choice == "rock" and p2_choice == "paper":
                result = "Player 1 Lose! and Player 2 win!"
                print("Result:", result)
                c = c + 1
            elif p1_choice == "paper" and p2_choice == "scissor":
                result = "Player 1 Lose! and Player 2 win!"
                print("Result:", result)
                c = c + 1
            elif p1_choice == "scissor" and p2_choice == "rock":
                result = "Player 1 Lose! and Player 2 win!"
                print("Result:", result)
                c = c + 1
            elif p1_choice == p2_choice:
                result = "Draw"
                print("Result:", result)
            else:
                result = "Player 1 Win! and Player 2 lose!"
                print("Result:", result)
                b = b + 1