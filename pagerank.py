import networkx as nx
import numpy as np

def pagerank_power_method(G, num_iter=100):
    M = get_google_matrix(G)
    n = M.shape[0]
    V = np.ones(n)/n
    for _ in range(num_iter):
        V = np.dot(M, V)
        
    return V

def pagerank_eigendecomposition(G, d=0.85):
    M = get_google_matrix(G, d=d)
    eigenvalues, eigenvectors = np.linalg.eig(M)
    index = eigenvalues.argsort()[-1]
    largest = np.array(eigenvectors[..., index]).flatten().real
    return largest/np.sum(np.abs(largest))

def get_google_matrix(G, d=0.85):
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
    print(get_google_matrix(G))
    
    pagerank_res = pagerank_power_method(G)
    pagerank_res = pagerank_eigendecomposition(G)
    print(pagerank_res)
    print(sum(pagerank_res))