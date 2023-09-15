"""EX01 - Chardle - A cute step toward Wordle."""
__author__= "730676929"

guess_word: str = input("Enter a 5-character word.")
guess_character: str = input("Enter a single character.")

if len(guess_word) != 5:
    print("Error: Word must contain 5 characters")

if len(guess_character) != 1:
    print("Error: character must be single character")

print("Searching for " + guess_character + " in " + guess_word)

instance: int = 0

if str(guess_word)[0] == str(guess_character):
    print(guess_character + " at index 0")
    instance = instance + 1
if str(guess_word)[1] == str(guess_character):
    print(guess_character + " at index 1 ")
    instance = instance + 1
if str(guess_word)[2] == str(guess_character):
    print(guess_character + " at index 2 ")
    instance = instance + 1
if str(guess_word)[3] == str(guess_character):
    print(guess_character + " at index 3 ")
    instance = instance + 1
if str(guess_word)[4] == str(guess_character):
    print(guess_character + " at index 4 ")
    instance = instance + 1

print(str(instance) + " instances of " + guess_character + " found in " + guess_word)

