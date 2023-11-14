"""EXO 6."""

__author__ = "730676929."


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Given a dictionary, invert the keys and its values."""
    inverted: dict[str, str] = {}
    for key in dict1:
        inverted[dict1[key]] = key
    return inverted


def favorite_color(dictcolor: dict[str, str]) -> str:
    """Given dictionary, return the most popular color."""
    most_popular: dict[str, int] = {}
    for key in dictcolor:
        if dictcolor[key] in most_popular:
            most_popular[dictcolor[key]] += 1
        else:
            most_popular[dictcolor[key]] = 1
    print(most_popular)
    first_value: int = 0
    top_color: str = ("")
    for key in most_popular:
        if int(most_popular[key]) > first_value:
            first_value = int(most_popular[key])
            top_color = key
    return top_color


def count(strings: list[str]) -> dict[str, int]:
    """Counts the freqency of the strings in the list."""
    store: dict[str, int] = {}
    for i in range(len(strings)):
        if strings[i] in store:
            store[strings[i]] += 1
        else:
            store[strings[i]] = 1
    return store


def alphabetizer(strings: list[str]) -> dict[str, list[str]]:
    """Function will produce a dict[str, list[str]] where each key is a unique letter in the alphabet and each value is a list of the words that begin with that letter."""
    alpha: dict[str, list[str]] = {}
    for i in range(len(strings)):
        if ((strings[i])[0]).lower() in alpha:
            alpha[((strings[i])[0]).lower()].append(strings[i])
        else:
            alpha[(strings[i])[0].lower()] = [strings[i]]
    return alpha
        

def update_attendance(dictionary: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Given a day and student, it will return the dictionary with updated attendance."""
    if day in dictionary:
        if student not in dictionary[day]:
            dictionary[day].append(student)
    else:
        dictionary[day] = [student]
    return dictionary
