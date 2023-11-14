"""Program that loop until correct number is guessed."""

from random import randint

secret: int = randint(1, 10)
guess: str = input("Guess a number between 1 and 10: ")
number_of_tries = 0
max_tries: int = 3

while (guess != secret) and (number_of_tries < max_tries - 1):
    print("Wrong") 
    # If guess is out of bounds, let them know
    if (guess < 1) or (guess > 10):
        print("That's not between 1 and 10")
    # If guess is too low, tell  them
    if guess < secret:
        print("Too low!")
    # IF guess is too high, tell them
    else:
        print("Too high!")
    # Ask for a different guess
    guess = int(input("Guess again: "))
    number_of_tries += 1
# If I've reached this point, guess = secret
if guess == secret:
    print("You guessed correctly")
else: 
    print("You lose!")