#   ROCK PAPER SCISSOR GAME WITH LOOPS AND BRANCHING

import random


#   welcome header!
space = 60
print()
print("~" * space)
print("Rock Paper Scissor Game".center(space))
print("~" * space)

#   computer list of choice
choice = ["r", "p", "s"]

#   multi-round
while True:
    computer_choice = random.choice(choice)

    #   computer friendly version
    if computer_choice == "r":
        computer_choice_full = "rock"
    elif computer_choice == "p":
        computer_choice_full = "paper"
    elif computer_choice == "s":
        computer_choice_full = "scissors"

    #   get user guess
    while True:
        user_choice = input("\nEnter your choice (r, p, s): ").lower()

        if user_choice == "r" or user_choice == "rock":
            user_choice_full = "rock"
            break
        elif user_choice == "p" or user_choice == "paper":
            user_choice_full = "paper"
            break
        elif user_choice == "s" or user_choice == "scissors":
            user_choice_full = "scissors"
            break
        else:
            print("Invalid choice. Please try again.")

    #   display computer and user choice
    print(f"You entered {user_choice_full}")
    print(f"Computer choose {computer_choice_full}")

    #   determine winner
    if user_choice_full == computer_choice_full:
        print("It's a tie!")
    elif user_choice_full == "rock" and computer_choice_full == "scissors":
        print("You win!")
    elif user_choice_full == "paper" and computer_choice_full == "rock":
        print("You win!")
    elif user_choice_full == "scissors" and computer_choice_full == "paper":
        print("You win!")
    else:
        print("Computer wins!")

    #   ask to play again
    again = input("\nPlay again? (y/n): ").lower()
    if again != "y":
        break
