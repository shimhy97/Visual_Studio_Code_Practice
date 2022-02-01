import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

#### inputs ####
wd = "G:/내 드라이브/고대2/admin/2021 location seminar/student"
ls_nodes = pd.read_csv(wd+"/ls_nodes.csv")
ls_links = pd.read_csv(wd+"/ls_links.csv")


#### actual Dikjstra ####
def Dijkstra(s, z, nodes, links):
    # <1> Initialization
    nodes["minDist"] = 9999
    nodes["PrevNode"] = int()
    # (a)
    nodes.at[s-1, "minDist"] = 0
    nodes.at[s-1, "PrevNode"] = 0
    # (b)
    nodes["scanned"] = int()
    # (c)
    nodes.at[s-1, "scanned"] = 1
    scanned_nodes = [s]

    while True:
        # <2> Label Updates
        ## (a)
        m = scanned_nodes[-1]
        ## (b)
        #### (1)
        Vm = nodes[nodes["Node"] == m].iloc[0]["minDist"]
        candidates = links[links["I"] == m]
        #### (2)
        for row in range(len(candidates)):
            j = candidates.iloc[row]["J"]
            if nodes[nodes["Node"] == j].iloc[0]["scanned"] == 1: next
            else: candidate_Tj = Vm + candidates.iloc[row]["length"]
            if candidate_Tj < nodes[nodes["Node"] == j].iloc[0]["minDist"]:
                nodes.loc[(nodes.Node == j), "minDist"] = candidate_Tj
                nodes.loc[(nodes.Node == j), "PrevNode"] = m

        # <3> Scan a Node
        ## (a)
        scanned_nodes.append(nodes.loc[nodes.loc[(nodes["scanned"] == 0),"minDist"].idxmin(),"Node"])
        nodes.loc[nodes.loc[(nodes["scanned"] == 0),"minDist"].idxmin(),"scanned"] = 1
        


        # <4> Termination Check
        if sum(nodes["scanned"]) == len(nodes): break
    print(nodes)
    shortest_path = [z]
    while True:
        this_step = shortest_path[0]
        if this_step == s: break
        prev_step = nodes.loc[nodes["Node"]==this_step,"PrevNode"].item()
        shortest_path.insert(0,prev_step)
    return (shortest_path)

#### plot network ####
G = nx.Graph()
G = nx.from_pandas_edgelist(ls_links, "I", "J", "length")
for row in range(len(ls_nodes)):
    G.add_node(ls_nodes.iloc[row][0], pos=(
        ls_nodes.iloc[row][1], ls_nodes.iloc[row][2]))

nx.draw(G, nx.get_node_attributes(G, "pos"), with_labels=True)
plt.show()  # plt.savefig(wd+"/nodes.png")

Dijkstra(1,8,ls_nodes,ls_links)