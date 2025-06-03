# standard_library.py
"""Python Essentials: The Standard Library.
Iris Coba
MTH420
04/14/2025
"""

from math import sqrt


# Problem 1
def prob1(L):
    """Return the minimum, maximum, and average of the entries of L
    (in that order, separated by a comma).
    """
    return min(L), max(L), sum(L)/len(L)


# Problem 2
def prob2():
    """Determine which Python objects are mutable and which are immutable.
    Test integers, strings, lists, tuples, and sets. Print your results.
    """
    int_1 = 10
    int_2 = int_1
    int_1 += 1
    print(int_1 == int_2) 
    
    str_1 = "hello"
    str_2 = str_1
    str_1 += " world"
    print(str_1 == str_2)

    list_1 = [1, 2, 3]
    list_2 = list_1
    list_1.append(4)
    print(list_1 == list_2)

    tuple_1 = (1, 2, 3)
    tuple_2 = tuple_1
    tuple_1 += (4,)
    print(tuple_1 == tuple_2)

    set_1 = {1, 2, 3}
    set_2 = set_1
    set_1.add(4)
    print(set_1 == set_2) 

    dict_1 = {1: 'x', 2: 'b'}
    dict_2 = dict_1
    dict_2[1] = 'a'
    print(dict_1 == dict_2)

    print("Lists, sets and dictionaries are mutable, while integers, strings and tuples are not.")


# Problem 3
from math import sqrt

def sum(a, b):
    return a + b

def product(a, b):
    return a * b
    
def hypot(a, b):
    """Calculate and return the length of the hypotenuse of a right triangle.
    Do not use any functions other than sum(), product() and sqrt() that are
    imported from your 'calculator' module.

    Parameters:
        a: the length one of the sides of the triangle.
        b: the length the other non-hypotenuse side of the triangle.
    Returns:
        The length of the triangle's hypotenuse.
    """ 
    a_squared = product(a, a)
    b_squared = product(b, b)
    sum_of_squares = cal.sum(a_squared, b_squared)
    hypotenuse = sqrt(sum_of_squares)
    return hypotenuse


# Problem 4
# In Python set objects are mutable and therefore unhashable and this means you can't add a set to another set.

from itertools import chain, combinations

def power_set(A):
    """Use itertools to compute the power set of A.

    Parameters:
        A (iterable): a str, list, set, tuple, or other iterable collection.

    Returns:
        (list(sets)): The power set of A as a list of sets.
    """
    items = list(A)
    return [set(subset) for r in range(len(items) + 1)
            for subset in combinations(items, r)]


# Problem 5: Implement shut the box.
def shut_the_box(player, timelimit):
    """Play a single game of shut the box."""
