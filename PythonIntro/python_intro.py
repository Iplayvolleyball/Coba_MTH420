# python_intro.py
"""Python Essentials: Introduction to Python.
Iris Coba
MTH420
04/11/2025
"""


# Problem 1 (write code below)
    
if __name__ == "__main__":
    print("Hello, world!")


# Problem 2
def sphere_volume(r):
    """ Return the volume of the sphere of radius 'r'.
    Use 3.14159 for pi in your computation.
    """
    return (4/3) * (3.14159) * r**3
    raise NotImplementedError("Problem 2 Incomplete")


# Problem 3
def isolate(a, b, c, d, e):
    """ Print the arguments separated by spaces, but print 5 spaces on either
    side of b.
    """
    print(f"{a}     {b}     {c} {d} {e}")
    raise NotImplementedError("Problem 3 Incomplete")

# Problem 4
def first_half(my_string):
    """ Return the first half of the string 'my_string'. Exclude the
    middle character if there are an odd number of characters.

    Examples:
        >>> first_half("python")
        'pyt'
        >>> first_half("ipython")
        'ipy'
    """
    return my_string[:len(my_string) // 2]
    raise NotImplementedError("Problem 4 Incomplete")

def backward(my_string):
    """ Return the reverse of the string 'my_string'.

    Examples:
        >>> backward("python")
        'nohtyp'
        >>> backward("ipython")
        'nohtypi'
    """
    return my_string[::-1]
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 5
def list_ops():
    """ Define a list with the entries "bear", "ant", "cat", and "dog".
    Perform the following operations on the list:
        - Append "eagle".
        - Replace the entry at index 2 with "fox".
        - Remove (or pop) the entry at index 1.
        - Sort the list in reverse alphabetical order.
        - Replace "eagle" with "hawk".
        - Add the string "hunter" to the last entry in the list.
    Return the resulting list.

    Examples:
        >>> list_ops()
        ['fox', 'hawk', 'dog', 'bearhunter']
    """
    my_list = ["bear", "ant", "cat", "dog"]
    my_list.append("eagle")
    my_list[2] = "fox"
    my_list.remove(my_list[1])
    my_list.sort(reverse = True)
    my_list[1] = "hawk"
    my_list.append("hunter")
    return my_list
    raise NotImplementedError("Problem 5 Incomplete")


# Problem 6
def pig_latin(word):
    """ Translate the string 'word' into Pig Latin, and return the new word.

    Examples:
        >>> pig_latin("apple")
        'applehay'
        >>> pig_latin("banana")
        'ananabay'
    """
    if word[0].lower() in "aeiou":
        return word + "hay"
    else:
        return word[1:] + word[0] + "ay"
    raise NotImplementedError("Problem 6 Incomplete")


# Problem 7
def palindrome():
    """ Find and retun the largest panindromic number made from the product
    of two 3-digit numbers.
    """
    max_palindrome = 0
    for i in range(999, 99, -1):
        for j in range(i, 99, -1): 
            product = i * j
            if str(product) == str(product)[::-1]:  
                if product > max_palindrome:
                    max_palindrome = product
    return max_palindrome
    raise NotImplementedError("Problem 7 Incomplete")

# Problem 8
def alt_harmonic(n):
    """ Return the partial sum of the first n terms of the alternating
    harmonic series, which approximates ln(2).
    """
    return sum([(-1) ** (k + 1) / k for k in range(1, n + 1)])
    raise NotImplementedError("Problem 8 Incomplete")

    
    
    
if __name__ == "__main__":
    print("Hello, world!")
    
#Test for Problem 2
print(sphere_volume(5))

#Test for Problem 3
print(isolate(1, 2, 3, 4, 5))

#Test for Problem 4
print(first_half("ciao"))
print(first_half("bella"))
print(backward("pizza"))
               
#Test for Problem 5
animals = list_ops()
print(animals)

#Test for Problem 6
print(pig_latin("cacca"))

#Test for Problem 7
print(palindrome())

#Test for Problem 8
print(alt_harmonic(500000))