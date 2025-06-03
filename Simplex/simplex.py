"""Volume 2: Simplex

Iris Coba
May 2025
MTH420
"""

import numpy as np

# Problems 1-6
class SimplexSolver(object):
    """Class for solving the standard linear optimization problem

                        minimize        c^Tx
                        subject to      Ax <= b
                                         x >= 0
    via the Simplex algorithm.
    """
    # Problem 1
    def __init__(self, c, A, b):
        """Check for feasibility and initialize the dictionary.

        Parameters:
            c ((n,) ndarray): The coefficients of the objective function.
            A ((m,n) ndarray): The constraint coefficients matrix.
            b ((m,) ndarray): The constraint vector.

        Raises:
            ValueError: if the given system is infeasible at the origin.
        """
        self.c = np.asarray(c)
        self.A = np.asarray(A)
        self.b = np.asarray(b)
        
        if not np.all(self.b >= 0):
            raise ValueError("The system is infeasible at the origin (Ax <= b fails at x = 0).")

    # Problem 2
    def _generatedictionary(self, c, A, b):
        """Generate the initial dictionary.

        Parameters:
            c ((n,) ndarray): The coefficients of the objective function.
            A ((m,n) ndarray): The constraint coefficients matrix.
            b ((m,) ndarray): The constraint vector.
        """
        m, n = A.shape

        dictionary = np.zeros((m + 1, n + m + 1))

        dictionary[:m, :n] = A       
        dictionary[:m, n:n + m] = np.eye(m)  
        dictionary[:m, -1] = b         

        dictionary[m, :n] = -c        

        return dictionary


    # Problem 3a
    def _pivot_col(self):
        """Return the column index of the next pivot column.
        """
        obj_row = self.dictionary[-1, :-1]  # Exclude RHS
        for i in range(len(obj_row)):
            if obj_row[i] < 0:
                return i  # Smallest index with negative coefficient
        return None

    # Problem 3b
    def _pivot_row(self, index):
        """Determine the row index of the next pivot row using the ratio test
        (Bland's Rule).
        """
        ratios = []
        for i in range(self.dictionary.shape[0] - 1):  # Skip last row (objective)
            col_val = self.dictionary[i, index]
            rhs_val = self.dictionary[i, -1]
            if col_val > 0:
                ratios.append((rhs_val / col_val, i))
        
        if not ratios:
            return None 
        
        ratios.sort()
        return ratios[0][1]

    # Problem 4
    def pivot(self):
        """Select the column and row to pivot on. Reduce the column to a
        negative elementary vector.
        """
        pivot_col_index = self._pivot_col()
        if pivot_col_index is None:
    
        pivot_column = self.dictionary[:-1, pivot_col_index]
        if np.all(pivot_column >= 0):
            raise ValueError("Problem is unbounded: no feasible direction to pivot.")
    
        pivot_row_index = self._pivot_row(pivot_col_index)
        if pivot_row_index is None:
            raise ValueError("Problem is unbounded: no valid pivot row found.")

        pivot_value = self.dictionary[pivot_row_index, pivot_col_index]
    
        self.dictionary[pivot_row_index, :] /= pivot_value
    
        for i in range(self.dictionary.shape[0]):
            if i != pivot_row_index:
                row_factor = self.dictionary[i, pivot_col_index]
                self.dictionary[i, :] -= row_factor * self.dictionary[pivot_row_index, :]

        return True

    # Problem 5
    def solve(self):
        """Solve the linear optimization problem.

        Returns:
            (float) The minimum value of the objective function.
            (dict): The basic variables and their values.
            (dict): The nonbasic variables and their values.
        """
        while True:
        if not self.pivot():
            break

        basic_vars = {}
        nonbasic_vars = {}
        m, n = self.A.shape

        for i in range(m):
            if i < n:
                basic_vars[i] = self.dictionary[i, -1]
            else:
                nonbasic_vars[i] = 0.0

        obj_value = self.dictionary[-1, -1]

        return obj_value, basic_vars, nonbasic_vars

# Problem 6
def prob6(filename='productMix.npz'):
    """Solve the product mix problem for the data in 'productMix.npz'.

    Parameters:
        filename (str): the path to the data file.

    Returns:
        ((n,) ndarray): the number of units that should be produced for each product.
    """
    data = np.load(filename)
    A = data['A']
    p = data['p']
    m = data['m']
    d = data['d']

    c = -p

    solver = SimplexSolver(c, A, m)
    obj_value, basic_vars, nonbasic_vars = solver.solve()

    production_quantities = np.zeros_like(c)
    for var, value in basic_vars.items():
        production_quantities[var] = value

    return production_quantities
