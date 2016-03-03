import random

def lotto(n, x, y):
    """ Generates a list of n numbers in range x-y, no duplicates. """
    a = random.sample(range(x, y + 1), n)
    return a