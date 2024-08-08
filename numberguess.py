import random

correct_guess = random.randint(1, 10)
user_guess = int(input("Guess the Number from 1 to 10: "))
if user_guess == correct_guess:
    print("You guessed it Right :) ")
elif user_guess>correct_guess:
    print(f"You guessed higher.{correct_guess}")
elif user_guess<correct_guess:
    print(f"You guessed lower.{correct_guess}")
else:
    print("Incorrect Guessing!")
