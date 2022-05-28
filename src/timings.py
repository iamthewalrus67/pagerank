"""
This is a module with code for the time comparisons for our data.
"""
import time
import pagerank
import networkx as nx


def time_pagerank(func, G):
    """
    Time a pagerank function.
    """
    t = time.time()
    data = func(G)
    time_res = time.time() - t

    return (data, time_res)


if __name__ == "__main__":
    G = nx.barabasi_albert_graph(100, 90)
    print(time_pagerank(pagerank.pagerank_power_method_no_eps, G))
    print(time_pagerank(pagerank.pagerank_eigendecomposition, G))
