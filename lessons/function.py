"""Demonstrates functions."""

print("Hello!")

print(round(10.25))


def mimic_letter(my_word: str, letter_idx: int):
    """Outputs the character of my_words at index letter_idx."""
    if letter_idx >= len(my_word):
        return ("index too high")
    # If we made it here, that means the letter_IDX IS VALID
    return my_word[letter_idx]


    