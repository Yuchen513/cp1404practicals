"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length

def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    car = Car("Test Car")
    assert car._odometer == 0, "Car does not set odometer correctly"

    # Test if Car sets the fuel correctly using default value
    default_car = Car("Default Car")
    assert default_car.fuel == 0, "Car does not set default fuel to 0"

    # Test if Car sets the fuel correctly when a value is provided
    custom_fuel_car = Car("Custom Fuel Car", fuel=10)
    assert custom_fuel_car.fuel == 10, "Car does not set custom fuel correctly"

run_tests()

def format_sentence(phrase):
    """
    Format a phrase as a sentence, starting with a capital letter and ending with a single full stop.
    >>> format_sentence('hello')
    'Hello.'
    >>> format_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_sentence('this is a test')
    'This is a test.'
    """
    phrase = phrase.strip()
    phrase = phrase[0].upper() + phrase[1:] if phrase else phrase
    if not phrase.endswith('.'):
        phrase += '.'
    return phrase
