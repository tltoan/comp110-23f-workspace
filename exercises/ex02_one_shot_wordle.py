"""One shot wordle."""

__author__: str = "730676929"

secret_word = "riley"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
guess: str = ""

while True:
    guess = input(f"What is your {len(secret_word)} letter guess?:")
    if (len(guess) == len(secret_word)):
        break  # Code enters a loop, where until the length of guess = the length of secret word
    else:  # If it does not equal one another it will prompt the user to try again
        print(f"That was not {len(secret_word)} letters! Try again:") 

result = ""
i = 0
while i < len(guess): 
    if guess[i] == secret_word[i]:  # If a letter in guess is right a green box will be add to the result
        result += GREEN_BOX
    else: 
        guessed_character_exists = False
        index = 0
        while not guessed_character_exists and index < len(secret_word):
            if secret_word[index] == guess[i]:
                guessed_character_exists = True
            else:
                index += 1
        if guessed_character_exists:
            result += YELLOW_BOX  # If a letter is partially correct it will add yellow box
        else:
            result += WHITE_BOX  # If a letter is not in the word it will add white box
    i += 1
if (guess) != secret_word:  # If user guesses it right it will print something, if they get it wrong it will print something
    print("Not quite. Play again soon!")
if (guess) == secret_word: 
    print("Woo! You got it!") 

print(result)