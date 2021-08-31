"""
utils.py contains a group of handfull methods that are used among
the tasks app.
"""
from random import choice


def random_word():
    """
    Return a random word from the given word list
    """
    words = ["Dr.Who", "Aquaman", "Superman", "Robin", "Batman", "KungFury"]
    return choice(words)

