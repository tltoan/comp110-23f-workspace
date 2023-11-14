"""Testing Dictionary of EXO6."""

__author__ = "831"

from exercises.ex06.dictionary import invert
from exercises.ex06.dictionary import favorite_color
from exercises.ex06.dictionary import count
from exercises.ex06.dictionary import alphabetizer
from exercises.ex06.dictionary import update_attendance


def test_invert_empty():
    """Empty invert list."""
    test_dict: dict[str, str] = {}
    assert invert(test_dict) == {}


def test_invert_str_str():
    """Given a dictionary, invert the keys and its values."""
    test_dictionary: dict[str, str] = {"apples": "dogs", 'oranges': 'cats', 'birds': 'bananas'}
    assert invert(test_dictionary)


def test_invert_float():
    """Test invert with float."""
    test_dict: dict[str, str] = {'apple': 3.1, 'blue': 3.1, 'red': 5.4}
    assert invert(test_dict) 


def test_favorite_color_empty():
    """Test favorite color empty list."""
    test_dict: dict[str, str] = {}
    assert favorite_color(test_dict) == ""


def test_favorite_color_input():
    """Test favorite color input."""
    test_dict: dict[str, str] = {'ezra': 'green', 'ryo': 'blue', 'keira': 'green'}
    assert favorite_color(test_dict) == "green"


def test_favorite_color_int():
    """Test favorite color with an interger."""
    test_dict: dict[str, str] = {'ezra': 1, 'ryo': 3, 'keira': 1}
    assert favorite_color(test_dict)
    

def test_count():
    """Test count input."""
    test_list: list[str] = ['ezra', 'keira', 'ryo', 'ezra',]
    test_dict: dict[str, int] = {'ezra': 2, 'keira': 1, 'ryo': 1}
    assert count(test_list) == test_dict


def test_count_empty():
    """Test count with empty list."""
    test_list: list[str] = []
    test_dict: dict[str, int] = {}
    assert count(test_list) == test_dict


def test_count_int():
    """Test count when list is an interger."""
    test_list: list[str] = [1, 3, 4, 8, 8, 6]
    test_dict: dict[str, int] = {1: 1, 3: 1, 4: 1, 8: 2, 6: 1}
    assert count(test_list) == test_dict


def test_alphabetizer():
    """Test alphabetizer with input."""
    test_list: list[str] = ['ezra', 'ethan', 'ryo', 'keira', 'ej', 'sarah']
    test_dict: dict[str, list[str]] = {'e': ['ezra', 'ethan', 'ej'], 'r': ['ryo'], 'k': ['keira'], 's': ['sarah']}
    assert alphabetizer(test_list) == test_dict


def test_alpjabetizer_empty():
    """Test alphabetizer with an empty input."""
    test_list: list[str] = []
    test_dict: dict[str, list[str]] = {}
    assert alphabetizer(test_list) == test_dict


def test_alphabetizer_float():
    """Test alphabetizer with number as strings."""
    test_list: list[str] = ['3.12', '3.145', '2.1', '2.5', '1.1']
    test_dict: dict[str, list[str]] = {'3': ['3.12', '3.145'], '2': ['2.1', '2.5'], '1': ['1.1']}
    assert alphabetizer(test_list) == test_dict


def test_update_attendance_empty():
    """Test update attendance with empty input."""
    test_dict: dict[str, list[str]] = {}
    test_day: str = ""
    test_student: str = ""
    test_result: dict[str, list[str]] = {'': ['']}
    assert update_attendance(test_dict, test_day, test_student) == test_result


def test_update_attendance_input():
    """Test update attendance with input dictionary."""
    test_dict: dict[str, list[str]] = {'monday': ['ezra', 'ryo'], 'tuesday': ['keira', 'sarah'], 'wednesday': ['erza', 'keira']}
    test_day: str = "monday"
    test_student: str = "keira"
    test_result: dict[str, list[str]] = {'monday': ['ezra', 'ryo', 'keira'], 'tuesday': ['keira', 'sarah'], 'wednesday': ['erza', 'keira']}
    assert update_attendance(test_dict, test_day, test_student) == test_result


def test_update_attendance_new_student():
    """Update attendance when there is a new student."""
    test_dict: dict[str, list[str]] = {'monday': ['ezra', 'ryo'], 'tuesday': ['keira', 'sarah'], 'wednesday': ['erza', 'keira']}
    test_day: str = "monday"
    test_student: str = "leon"
    test_result: dict[str, list[str]] = {'monday': ['ezra', 'ryo', 'leon'], 'tuesday': ['keira', 'sarah'], 'wednesday': ['erza', 'keira']}
    assert update_attendance(test_dict, test_day, test_student) == test_result