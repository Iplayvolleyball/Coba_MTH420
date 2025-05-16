# numpy_intro.py
"""Python Essentials: Intro to NumPy.
Iris Coba
04/21/2025
MTH420
"""

import numpy as np


def prob1():
    """ Define the matrices A and B as arrays. Return the matrix product AB. """
    A = np.array([[3, -1, 4], [1, 5, -9]])
    B = np.array([[2, 6, -5, 3], [5, -8, 9, 7], [9, -3, -2, -3]])
    return A @ B
    raise NotImplementedError("Problem 1 Incomplete")

#idk probably not right, it gives that the result is the 0 matrix
def prob2():
    """ Define the matrix A as an array. Return the matrix -A^3 + 9A^2 - 15A. """
    A = np.array([[3, 1, 4], [1, 5, 9], [-5, 3, 1]])
    return -1 * (A @ A @ A) + 9 * (A @ A) - 15 * A
    raise NotImplementedError("Problem 2 Incomplete")


def prob3():
    """ Define the matrices A and B as arrays using the functions presented in
    this section of the manual (not np.array()). Calculate the matrix product ABA,
    change its data type to np.int64, and return it.
    """
    A = np.triu(np.ones((7, 7)) * 1)
    upper = np.triu(A)
    
    B = np.full((7, 7), 5)
    B[np.tril_indices(7)] = -1
    
    ABA = A @ B @ A
    ABA_int = ABA.astype(np.int64)
    
    return (ABA_int)
    raise NotImplementedError("Problem 3 Incomplete")


def prob4(A):
    """ Make a copy of 'A' and use fancy indexing to set all negative entries of
    the copy to 0. Return the resulting array.
    
    Example:
        >>> A = np.array([-3,-1,3])
        >>> prob4(A)
        array([0, 0, 3])
    """
    B = A.copy()         
    B[B < 0] = 0         
    return B
    raise NotImplementedError("Problem 4 Incomplete")


def prob5():
    #Remeber to resize the zero matrices based on matrices around it. 
    """ Define the matrices A, B, and C as arrays. Use NumPy's stacking functions
    to create and return the block matrix:
                                | 0 A^T I |
                                | A  0  0 |
                                | B  0  C |
    where I is the 3x3 identity matrix and each 0 is a matrix of all zeros
    of the appropriate size.
    """
    A = np.array([[0, 2, 4], [1, 3, 5]])
    B = np.array([[3, 0, 0], [3, 3, 0], [3, 3, 3]])
    C = np.array([[-2, 0, 0], [0, -2, 0], [0, 0, -2]])
    I = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    Z_3x3 = np.zeros((3, 3))
    Z_2x2 = np.zeros((2, 2))
    Z_2x3 = np.zeros((2, 3))
    Z_3x2 = np.zeros((3, 2))
    
    column_1 = np.vstack((Z_3x3, A, B))
    column_2 = np.vstack((A.T, Z_2x2, Z_3x2))
    column_3 = np.vstack((I, Z_2x3, C))
    block_matrix = np.hstack((column_1, column_2, column_3))
    return block_matrix
    raise NotImplementedError("Problem 5 Incomplete")


def prob6(A):
    """ Divide each row of 'A' by the row sum and return the resulting array.
    Use array broadcasting and the axis argument instead of a loop.

    Example:
        >>> A = np.array([[1,1,0],[0,1,0],[1,1,1]])
        >>> prob6(A)
        array([[ 0.5       ,  0.5       ,  0.        ],
               [ 0.        ,  1.        ,  0.        ],
               [ 0.33333333,  0.33333333,  0.33333333]])
    """
    row_sums = A.sum(axis=1).reshape(-1,1)
    return A / row_sums


# How do I put the file grid.npy in the current directory?

grid = np.load("grid.npy")

def prob7(grid):
    """ Given the array stored in grid.npy, return the greatest product of four
    adjacent numbers in the same direction (up, down, left, right, or
    diagonally) in the grid. Use slicing, as specified in the manual.
    """
    max_product = 0
    rows, cols = grid.shape

    for r in range(rows):
        for c in range(cols):
            # Horizontal (→)
            if c + 3 < cols:
                max_product = max(max_product, np.prod(grid[r, c:c+4]))

            # Vertical (↓)
            if r + 3 < rows:
                max_product = max(max_product, np.prod(grid[r:r+4, c]))

            # Diagonal (↘)
            if r + 3 < rows and c + 3 < cols:
                max_product = max(max_product, np.prod([grid[r+i, c+i] for i in range(4)]))

            # Anti-diagonal (↙)
            if r + 3 < rows and c - 3 >= 0:
                max_product = max(max_product, np.prod([grid[r+i, c-i] for i in range(4)]))

    return max_product
    raise NotImplementedError("Problem 7 Incomplete")
