# cvxpy_intro.py
"""Volume 2: Intro to CVXPY.
Iris Coba
MTH420
05/30/2025
"""

import numpy as np
import cvxpy as cp

def prob1():
    """Solve the following convex optimization problem:

    minimize        2x + y + 3z
    subject to      x  + 2y         <= 3
                         y   - 4z   <= 1
                    2x + 10y + 3z   >= 12
                    x               >= 0
                          y         >= 0
                                z   >= 0

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    x1 = cp.Variable()
    x2 = cp.Variable()
    x3 = cp.Variable()

    objective = cp.Minimize(2*x1 + x2 + 3*x3)

    constraints = [
        x1 + 2*x2 <= 3,          
        x2 - 4*x3 <= 1,            
        2*x1 + 10*x2 + 3*x3 >= 12, 
        x1 >= 0,                   
        x2 >= 0,                   
        x3 >= 0                   
    ]

    problem = cp.Problem(objective, constraints)

    problem.solve()

    return np.array([x1.value, x2.value, x3.value]), problem.value


# Problem 2
def l1Min(A, b):
    """Calculate the solution to the optimization problem

        minimize    ||x||_1
        subject to  Ax = b

    Parameters:
        A ((m,n) ndarray)
        b ((m, ) ndarray)

    Returns:
        The optimizer x (ndarray)
        The optimal value (float)
    """
    x = cp.Variable(A.shape[1])

    objective = cp.Minimize(cp.norm(x, 1))

    constraints = [A @ x == b]

    problem = cp.Problem(objective, constraints)

    problem.solve()

    return x.value, problem.value
    

# Problem 3
def prob3():
    """Solve the transportation problem by converting the last equality constraint
    into inequality constraints.

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    p1 = cp.Variable()  
    p2 = cp.Variable()  
    p3 = cp.Variable()  
    p4 = cp.Variable()  
    p5 = cp.Variable()  
    p6 = cp.Variable()  

    objective = cp.Minimize(4*p1 + 7*p2 + 6*p3 + 8*p4 + 8*p5 + 9*p6)

    constraints = [
        p1 + p2 == 7,    
        p3 + p4 == 2,   
        p5 + p6 == 4,    
        p1 + p3 + p5 == 5,  
        p2 + p4 + p6 == 8,  
        p1 >= 0, p2 >= 0, p3 >= 0, p4 >= 0, p5 >= 0, p6 >= 0 
    ]

    problem = cp.Problem(objective, constraints)

    problem.solve()

    optimizer = np.array([p1.value, p2.value, p3.value, p4.value, p5.value, p6.value])
    return optimizer, problem.value


from scipy.optimize import minimize

# Problem 4
def prob4():
    """Find the minimizer and minimum of

    g(x,y,z) = (3/2)x^2 + 2xy + xz + 2y^2 + 2yz + (3/2)z^2 + 3x + z

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    def g(x):
        x1, x2, x3 = x
        return 23 * x1**2 + 2 * x1 * x2 + x1 * x3 + 2 * x2**2 + 2 * x2 * x3 + 23 * x3**2 + 3 * x1 + x3

   
    def grad_g(x):
        x1, x2, x3 = x
        grad_x1 = 46 * x1 + 2 * x2 + x3 + 3
        grad_x2 = 2 * x1 + 4 * x2 + 2 * x3
        grad_x3 = x1 + 2 * x2 + 46 * x3 + 1
        return np.array([grad_x1, grad_x2, grad_x3])
   
        initial_guess = np.array([0, 0, 0])
    
        result = minimize(g, initial_guess, jac=grad_g, method='Newton-CG')
        minimum_value = result.fun

        return minimizer, minimum_value
    

# Problem 5
def prob5(A, b):
    """Calculate the solution to the optimization problem
        minimize    ||Ax - b||_2
        subject to  ||x||_1 == 1
                    x >= 0
    Parameters:
        A ((m,n), ndarray)
        b ((m,), ndarray)
        
    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    n = A.shape[1]

    x = cp.Variable(n, nonneg=True)

    objective = cp.Minimize(cp.norm(A @ x - b, '2'))

    constraints = [cp.norm(x, 1) == 1]

    problem = cp.Problem(objective, constraints)
    problem.solve()

    return x.value, problem.value


# Problem 6
def prob6():
    """Solve the college student food problem. Read the data in the file 
    food.npy to create a convex optimization problem. The first column is 
    the price, second is the number of servings, and the rest contain
    nutritional information. Use cvxpy to find the minimizer and primal 
    objective.
    
    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """	 
    raise NotImplementedError("Problem 6 Incomplete")