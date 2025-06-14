# drazin.py
"""Volume 1: The Drazin Inverse.
Iris Coba
MTH420
05/15/2025
"""

import numpy as np
from scipy import linalg as la


# Helper function for problems 1 and 2.
def index(A, tol=1e-5):
    """Compute the index of the matrix A.

    Parameters:
        A ((n,n) ndarray): An nxn matrix.

    Returns:
        k (int): The index of A.
    """

    # test for non-singularity
    if not np.isclose(la.det(A), 0):
        return 0

    n = len(A)
    k = 1
    Ak = A.copy()
    while k <= n:
        r1 = np.linalg.matrix_rank(Ak)
        r2 = np.linalg.matrix_rank(np.dot(A,Ak))
        if r1 == r2:
            return k
        Ak = np.dot(A,Ak)
        k += 1

    return k


# Problem 1
def is_drazin(A, Ad, k):
    """Verify that a matrix Ad is the Drazin inverse of A.

    Parameters:
        A ((n,n) ndarray): An nxn matrix.
        Ad ((n,n) ndarray): A candidate for the Drazin inverse of A.
        k (int): The index of A.

    Returns:
        (bool) True of Ad is the Drazin inverse of A, False otherwise.
    """
    condition1 = np.allclose(A @ Ad, Ad @ A)
    condition2 = np.allclose(np.linalg.matrix_power(A, k+1) @ Ad, np.linalg.matrix_power(A, k))
    condition3 = np.allclose(Ad @ A @ Ad, Ad)

    return condition1 and condition2 and condition3


# Problem 2
def drazin_inverse(A, tol=1e-4):
    """Compute the Drazin inverse of A.

    Parameters:
        A ((n,n) ndarray): An nxn matrix.

    Returns:
       ((n,n) ndarray) The Drazin inverse of A.
    """
    n = A.shape[0]
    T, Q, k = la.schur(A, sort=lambda x: abs(x) > tol)
    U = Q.copy()

    T11 = T[:k, :k]
    T22 = T[k:, k:]
    if k > 0:
        T11_inv = np.linalg.inv(T11)
    else:
        T11_inv = np.zeros((0, 0))
    Z = np.zeros_like(A)
    Z[:k, :k] = T11_inv

    Ad = U @ Z @ np.linalg.inv(U)
    return Ad


# Problem 3
def effective_resistance(A):
    """Compute the effective resistance for each node in a graph.

    Parameters:
        A ((n,n) ndarray): The adjacency matrix of an undirected graph.

    Returns:
        ((n,n) ndarray) The matrix where the ijth entry is the effective
        resistance from node i to node j.
    """
    n = A.shape[0]
    
    D = np.diag(np.sum(A, axis=1))
    
    L = D - A
    
    L_pinv = np.linalg.pinv(L)
    
    R = np.zeros((n, n))
    
    for i in range(n):
        for j in range(n):
            R[i, j] = L_pinv[i, i] + L_pinv[j, j] - 2 * L_pinv[i, j]
    
    return R


# Problems 4 and 5
class LinkPredictor:
    """Predict links between nodes of a network."""

    def __init__(self, filename='social_network.csv'):
        """Create the effective resistance matrix by constructing
        an adjacency matrix.

        Parameters:
            filename (str): The name of a file containing graph data.
        """
        raise NotImplementedError("Problem 4 Incomplete")


    def predict_link(self, node=None):
        """Predict the next link, either for the whole graph or for a
        particular node.

        Parameters:
            node (str): The name of a node in the network.

        Returns:
            node1, node2 (str): The names of the next nodes to be linked.
                Returned if node is None.
            node1 (str): The name of the next node to be linked to 'node'.
                Returned if node is not None.

        Raises:
            ValueError: If node is not in the graph.
        """
        raise NotImplementedError("Problem 5 Incomplete")


    def add_link(self, node1, node2):
        """Add a link to the graph between node 1 and node 2 by updating the
        adjacency matrix and the effective resistance matrix.

        Parameters:
            node1 (str): The name of a node in the network.
            node2 (str): The name of a node in the network.

        Raises:
            ValueError: If either node1 or node2 is not in the graph.
        """
        raise NotImplementedError("Problem 5 Incomplete")
