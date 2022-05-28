"""
This module contains all the methods needed to compute the pagerank of a graph.
"""

import networkx as nx
import numpy as np


def pagerank_power_method_no_eps(G, num_iter=100):
    """
    Regular power method that just runs for a fixed number of iterations.

    Parameters
    ----------
    G : list
        An adjacency matrix that gets turned into the
        Google matrix with the get_google_matrix function
    num_iter : int, optional
        The number of iterations the pagerank fucntion will run

    Returns
    -------
    np.array
        An eigenvector with the pagerank values for each node.
    """
    M = get_google_matrix(G)

    n = M.shape[0]
    V = np.ones(n)/n

    for _ in range(num_iter):
        V = np.dot(M, V)

    return V



def pagerank_power_method_w_eps(G, num_iter=100, eps=10**(-8)):
    """
    Regular power method that has iterations and epsilon, can bw
    slower that the non-epsilon method with perfect number of iterations due to
    array copying.

    Parameters
    ----------
    G : list
        An adjacency matrix that gets turned into the
        Google matrix with the get_google_matrix function
    num_iter : int, optional
        The number of iterations the pagerank fucntion will run

    Returns
    -------
    np.array
        An eigenvector with the pagerank values for each node.
    """
    M = get_google_matrix(G)

    n = M.shape[0]
    V = np.ones(n)/n

    for _ in range(num_iter):
        prevV = V.copy()
        V = np.dot(M, V)
        if all(abs(V - prevV) < eps):
            break

    return V


def pagerank_eigendecomposition(G):
    """
    Eigendecomposition method - just finds the dominant eigenvector of G, more complex
    that the power method with complexity O(n^3).

    Parameters
    ----------
    G : list
        An adjacency matrix that gets turned into the
        Google matrix with the get_google_matrix function

    Returns
    -------
    ndarray
        An eigenvector with the pagerank values for each node.
    """
    M = get_google_matrix(G)

    eigenvalues, eigenvectors = np.linalg.eig(M)
    index = eigenvalues.argsort()[-1]

    largest = np.array(eigenvectors[..., index]).flatten().real

    return largest/np.sum(np.abs(largest))


def get_google_matrix(G, d=0.85):
    """
    Transforms the given anjacency matrix G into the google matrix by 
    connecting the sink nodes and turning the matrix into stochastic matrix.

    Parameters
    ----------
    G : list
        An adjacency matrix
    d: int, optional
        The damping factor, or te possibility of resetting out theoretical random unbiased
        web surfer

    Returns
    -------
    ndarray
        A stochastic google matrix with no sinking nodes.
    """
    A = nx.to_numpy_array(G).T
    n = A.shape[0]

    is_node_sink = np.sum(A, axis=0) == 0 # array of booleans
    # Add virtual edges from sink nodes to all other nodes
    B = (np.ones(n) - np.identity(n)) / (n-1)
    A[..., is_node_sink] += B[..., is_node_sink]

    # Inverse degree matrix
    D_inv = np.diag(1/np.sum(A, axis=0))
    # Transition matrix
    M = np.dot(A, D_inv)

    # For disconnected components
    M = d * M + (1-d) * np.ones(n)/n
    return M

if __name__ == "__main__":
    G = nx.barabasi_albert_graph(5, 4)
    
    pagerank_res = pagerank_power_method_no_eps(G)
    print("Power method no eps: ", pagerank_res)
    pagerank_res = pagerank_power_method_w_eps(G)
    print("Power method with eps: ", pagerank_res)
    pagerank_res = pagerank_eigendecomposition(G)
    print("Eigendecomposition method: ", pagerank_res)