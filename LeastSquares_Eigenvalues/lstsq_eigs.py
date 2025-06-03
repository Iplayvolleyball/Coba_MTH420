# lstsq_eigs.py
"""Volume 1: Least Squares and Computing Eigenvalues.
Iris Coba
MTH420
5/7/2025
"""

import numpy as np
from cmath import sqrt
from scipy import linalg as la
from matplotlib import pyplot as plt


# Problem 1
def least_squares(A, b):
    """Calculate the least squares solutions to Ax = b by using the QR
    decomposition.

    Parameters:
        A ((m,n) ndarray): A matrix of rank n <= m.
        b ((m, ) ndarray): A vector of length m.

    Returns:
        x ((n, ) ndarray): The solution to the normal equations.
    """
    Q, R = la.qr(A, mode="economic")
    
    Qt_b = Q.T @ b
    
    x = la.solve_triangular(R, Qt_b)

    return x

# Problem 2
def least_squares(A, b):
    Q, R = la.qr(A, mode="economic")
    Qt_b = Q.T @ b
    x = la.solve_triangular(R, Qt_b)
    return x

def line_fit():
    """Find and plot the least squares line that relates year to housing index."""
    # Load data
    data = np.load("housing.npy")
    years = data[:, 0]
    index = data[:, 1]
    
    A = np.column_stack((np.ones_like(years), years))
    
    b = index

    coeffs = least_squares(A, b)
    c0, c1 = coeffs

    plt.scatter(years, index, label="Data", color="blue")

    x_vals = np.linspace(min(years), max(years), 100)
    y_vals = c0 + c1 * x_vals
    plt.plot(x_vals, y_vals, label="Least Squares Line", color="red")

    # Labels and legend
    plt.xlabel("Year (0 = 2000)")
    plt.ylabel("Housing Price Index")
    plt.title("Least Squares Fit to Housing Data")
    plt.legend()
    plt.grid(True)
    plt.show()
    


# Problem 3
def polynomial_fit():
    """Find the least squares polynomials of degree 3, 6, 9, and 12 that relate
    the year to the housing price index for the data in housing.npy. Plot both
    the data points and the least squares polynomials in individual subplots.
    """
    data = np.load("housing.npy")
    x = data[:, 0]
    y = data[:, 1]
    degrees = [3, 6, 9, 12]
    x_fine = np.linspace(x.min(), x.max(), 500)

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    axes = axes.flatten()

    for i, deg in enumerate(degrees):
        A = np.vander(x, deg + 1, increasing=True)
        coeffs = la.lstsq(A, y)[0]
        A_fine = np.vander(x_fine, deg + 1, increasing=True)
        y_fit = A_fine @ coeffs

        ax = axes[i]
        ax.scatter(x, y, color='blue', label="Data")
        ax.plot(x_fine, y_fit, color='red', label=f"Degree {deg}")
        ax.set_title(f"Polynomial Degree {deg}")
        ax.set_xlabel("Year (0 = 2000)")
        ax.set_ylabel("Housing Index")
        ax.grid(True)
        ax.legend()

    plt.tight_layout()
    plt.show()


def plot_ellipse(a, b, c, d, e):
    """Plot an ellipse of the form ax^2 + bx + cxy + dy + ey^2 = 1."""
    theta = np.linspace(0, 2*np.pi, 200)
    cos_t, sin_t = np.cos(theta), np.sin(theta)
    A = a*(cos_t**2) + c*cos_t*sin_t + e*(sin_t**2)
    B = b*cos_t + d*sin_t
    r = (-B + np.sqrt(B**2 + 4*A)) / (2*A)

    plt.plot(r*cos_t, r*sin_t)
    plt.gca().set_aspect("equal", "datalim")

# Problem 4
def ellipse_fit():
    """Calculate the parameters for the ellipse that best fits the data in
    ellipse.npy. Plot the original data points and the ellipse together, using
    plot_ellipse() to plot the ellipse.
    """
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 5
def power_method(A, N=20, tol=1e-12):
    """Compute the dominant eigenvalue of A and a corresponding eigenvector
    via the power method.

    Parameters:
        A ((n,n) ndarray): A square matrix.
        N (int): The maximum number of iterations.
        tol (float): The stopping tolerance.

    Returns:
        (float): The dominant eigenvalue of A.
        ((n,) ndarray): An eigenvector corresponding to the dominant
            eigenvalue of A.
    """
    raise NotImplementedError("Problem 5 Incomplete")


# Problem 6
def qr_algorithm(A, N=50, tol=1e-12):
    """Compute the eigenvalues of A via the QR algorithm.

    Parameters:
        A ((n,n) ndarray): A square matrix.
        N (int): The number of iterations to run the QR algorithm.
        tol (float): The threshold value for determining if a diagonal S_i
            block is 1x1 or 2x2.

    Returns:
        ((n,) ndarray): The eigenvalues of A.
    """
    raise NotImplementedError("Problem 6 Incomplete")
