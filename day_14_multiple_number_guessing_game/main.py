#   MULTIPLE NUMBER GUESSING GAME
#   LIMITATIONS: not user proof

import random

high_number = 10
number_of_guesses = 4

#   generate random number
random_number = random.randint(1, 10)


#   header formatting, welcome!
space = 60
print()
print("?" * space)
print()
print("Multiple Number Guessing Game".center(space))
print()
print("?" * space)
print()
print(f"You only have {number_of_guesses - 1} guess".center(space))
print()


for guess in range(1, number_of_guesses):
    #   display what guess are you on
    print(f"\nGUESS NUMBER: {guess}")

    #   get user input (guess)
    user_guess = int(input("Guess a number between 1 and 10: "))

    #   check the guess
    if user_guess == random_number:
        print(f"\nCORRECT, THE SECRET NUMBER IS: {user_guess}")
        break
    elif user_guess > random_number:
        print("\nTOO HIGH")
    elif user_guess < random_number:
        print("\nTOO LOW")

    if guess == 3:
        print("\nYou didn't guess the secret number. Bye!")
        break

print(f"The secret number is: {random_number}")
print("Thank you for playing!")
