## This Code is Sample of GGNN (Graph Neural Network)

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import matplotlib.pyplot as plt
import networkx as nx
import random
import math
import time

# Define Weighted Digraph model with cost
def make_graph(num_node):
    G = nx.Graph()
    G.add_nodes_from(range(num_node))
    for i in range(num_node):
        for j in range(i+1, num_node):
            G.add_edge(i, j, weight=random.randint(1, 10))
    # Give random cost to each node
    for i in range(num_node):
        G.nodes[i]['cost'] = random.randint(1, 10)
    return G
###
##################
3################
# save graph as image
def save_graph(G, name):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    plt.savefig(name)
    plt.close()

# Define Graph Neural Network with pytorch
class GGNN(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, num_step):
        super(GGNN, self).__init__()
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.output_dim = output_dim
        self.num_step = num_step

        self.W_i = nn.Linear(self.input_dim, self.hidden_dim)
        self.W_h = nn.Linear(self.hidden_dim, self.hidden_dim)
        self.W_o = nn.Linear(self.hidden_dim, self.output_dim)

        self.U_i = nn.Linear(self.input_dim, self.hidden_dim)
        self.U_h = nn.Linear(self.hidden_dim, self.hidden_dim)
        self.U_o = nn.Linear(self.hidden_dim, self.output_dim)
    
    def forward(self, x, adj):
        h = torch.zeros(x.size(0), self.hidden_dim)
        c = torch.zeros(x.size(0), self.hidden_dim)
        for i in range(self.num_step):
            m = torch.mm(adj, h)
            h = torch.tanh(self.W_i(x) + self.W_h(h) + self.U_i(x) + self.U_h(m))
            c = c + h
        o = self.W_o(h) + self.U_o(c)
        return o
    
# Predict
def predict(model, x, adj):
    model.eval()
    with torch.no_grad():
        output = model(x, adj)
    return output

# Train
def train(model, x, adj, y, optimizer):
    model.train()
    optimizer.zero_grad()
    output = model(x, adj)
    loss = F.cross_entropy(output, y)
    loss.backward()
    optimizer.step()
    return loss

### Main ###
def main():
    # Define Graph
    G = make_graph(num_node = 5)
    # save graph as image, name has date and time
    save_graph(G, "graphInput_"+time.strftime("%Y%m%d_%H%M")+".png")
    # Define Adjacency Matrix with cost
    adj = torch.FloatTensor(nx.to_numpy_matrix(G, weight='weight'))
 

    # Define Model
    inputDict = {'input_dim': 1, 'hidden_dim': 10, 'output_dim': 2, 'num_step': 5}
    model = GGNN(**inputDict)
    optimizer = optim.Adam(model.parameters(), lr=0.01)

    

    # Graph Visualization
    nx.draw(G, with_labels=True)
    plt.show()
    # output visualization
    print("output: ", output)
    # Save
    plt.savefig("graph.png")

if __name__ == "__main__":
    main()
