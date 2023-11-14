"""Structured Wordle."""

__author__: str = "730676929"


def contains_char(word: str, char: str) -> bool:
    """Takes two strongs as a parameter and returns a boolean."""
    # Assert that the second parameter is a single character
    assert len(char) == 1
    # Loop through each character of the first parameter
    for character in word: 
        # If the character matches the second parameter, return True
        if char == character:
            return True
    # In no match is found, return False
    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str: 
    """Returns strings as emoji's correlating to letters."""
    assert len(guess) == len(secret)
    emoji_string = ""
    for i in range(len(guess)):
        guess_char = guess[i]
        secret_char = secret[i]
        if guess_char == secret_char:
            emoji_string += GREEN_BOX 
        elif contains_char(secret, guess_char):
            emoji_string += YELLOW_BOX
        else:
            emoji_string += WHITE_BOX
    return emoji_string


def input_guess(expected_length: int) -> str:
    """Takes an interger as a parameter and promts user for that guess word length, continues to prompt until length is given."""
    user_input = ""
    while len(user_input) != expected_length: 
        user_input = input(f"Enter a {expected_length} character word: ")  # Prompts player to enter a word
        if len(user_input) == expected_length:
            return user_input               
        else:
            print(f"That wasn't {expected_length} chars! Try again:")  # If it wasn't the right length, prompt them again
    return str(user_input)


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret = "fatty"  # Secret word
    max_turns = 6
    current_turns = 1
    won = False

    while current_turns <= max_turns and not won: 
        print(f"===Turn {current_turns}/{max_turns}===")
        guess = input_guess(len(secret))  # Variable that adapts to length of word
        emoji_string = emojified(guess, secret)  # Activate the emojified function
        print(emoji_string) 
        if guess == secret:
            won = True
        else:
            current_turns += 1 

        if won:
            print(f"You won in {current_turns}/{max_turns}")  # If won print you won in X/6, where is X is the number of turns user took to win
            exit
        else:
            if current_turns > max_turns:
                print(f"X/{max_turns} - Sorry, try again tommorow!")  # Print X/6, "sorry, try again tommorow" where X is 6


if __name__ == "__main__":
    main()