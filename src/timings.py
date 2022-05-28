"""
This is a module with code for the time comparisons for our data.
"""
import time
import pagerank
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as col

COLORS = ["#dd95ff", "#95d5ff", "#95ffca", "#ebb240", "#df4a6c"]
LABELS = ["power method without epsilon",
          "eigendecomposition method",
          "power method with epsilon",
          "nx library pagerank"]


def time_pagerank(func, G, num_runs):
    """
    Time a pagerank function.
    """
    data = []
    t = time.time()
    for _ in range(num_runs):
        data = func(G)
    time_res = (time.time() - t) / num_runs

    return data, time_res


def draw_plot(x, *yy):
    fig, ax = plt.subplots()
    for i in range(len(yy)):
        _, = plt.plot(x, yy[i], linewidth=2.0, color=COLORS[i], label=LABELS[i])
    c = col.to_rgba("#94fce1", 0.05)
    ax.set_facecolor(c)
    ax.set_ylabel('time (s)')
    ax.set_xlabel('nodes in G graph')
    ax.set_title('base graph')
    leg = plt.legend(loc='upper left')
    plt.show()


if __name__ == "__main__":
    pagerank_power_method_no_eps_timings = []
    pagerank_power_method_eps_timings = []
    pagerang_eigendecomposition_timing = []
    pagerank_nx_timing = []

    samples = [[100, 50], [200, 100], [400, 200], [800, 400], [1600, 800]]
    num_runs = 20

    for s in samples:
        G = nx.barabasi_albert_graph(s[0], s[1])
        pagerank_power_method_no_eps_timings.append(
            time_pagerank(pagerank.pagerank_power_method_no_eps, G, num_runs)[1])
        pagerang_eigendecomposition_timing.append(
            time_pagerank(pagerank.pagerank_eigendecomposition, G, num_runs)[1])
        pagerank_power_method_eps_timings.append(
            time_pagerank(pagerank.pagerank_power_method_w_eps, G, num_runs)[1])
        pagerank_nx_timing.append(
            time_pagerank(nx.pagerank, G, num_runs)[1])

    draw_plot([100, 200, 400, 800, 1600],
              pagerank_power_method_no_eps_timings,
              pagerang_eigendecomposition_timing,
              pagerank_power_method_eps_timings,
              pagerank_nx_timing)

    print()
