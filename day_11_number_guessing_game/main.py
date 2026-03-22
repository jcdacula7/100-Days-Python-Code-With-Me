#   NUMBER GUESSING GAME
#   LIMITATIONS: not user proof, very simple

import random

#   generate random number
random_number = random.randint(1, 10)


#   header formatting, welcome!
space = 60
print()
print("?" * space)
print()
print("Number Guessing Game".center(space))
print()
print("?" * space)
print()


#   get user input (guess)
user_guess = int(input("Guess a number between 1 and 10: "))


#   check the guess
if user_guess == random_number:
    print(f"Correct, your guess is: {user_guess}")
elif user_guess > random_number:
    print("Too high")
elif user_guess < random_number:
    print("Too low")
else:
    print("Invalid guess")


print(f"\nThe secret number is: {random_number}")
print("Thank you for playing")
