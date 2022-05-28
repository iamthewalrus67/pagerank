import networkx as nx
import pagerank

def parse_hollins_dataset(path):
    """
    Parse data from Hollins University dataset.

    Returns networkx graph and dictionart of websites with their corresponding indexes.
    """
    G = nx.Graph()
    site_dict = dict()
    with open(path, "r") as f:
        f.readline()
        while True:
            line = f.readline()

            if not line:
                break

            a, b = line.strip().split()
            a = int(a)
            try:
                b = int(b)
                G.add_edge(a, b)
            except:
                site_dict[a] = b

    return G, site_dict

if __name__ == "__main__":
    import time
    import pagerank
    
    G, site_dict = parse_hollins_dataset("data/in.txt")
    start = time.time()
    pagerank_res = pagerank.pagerank_power_method_w_eps(G)
    end = time.time() - start
    print(f"Time taken by PageRank: {end}")
    result_dict = dict()

    for index, res in enumerate(pagerank_res):
        result_dict[site_dict[index+1]] = res

    result_dict = sorted(result_dict.items(), reverse=True, key=lambda item: item[1])

    with open("data/out.txt", "w") as f:
        out_str = ""
        for index, res in enumerate(result_dict):
            out_str += f"{res[0]} " + "{:.8f}".format(res[1]) + "\n"

        f.write(out_str)    