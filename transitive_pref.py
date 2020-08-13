#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 12:48:15 2020

@author: neilhacker
"""
import itertools
import random
import networkx as nx 
import matplotlib.pyplot as plt
from collections import defaultdict 

options = ['tulum', 'tokyo', 'venice', 'rome','NYC', 'cape town','athens','brussels']

x = itertools.combinations(options,2)

combins = []
for i in x:
    combins.append(i)
random.shuffle(combins)    

directed_edges = [] 

# gets user to rank pairs of options and then updates directed edges for graph later
# and also g so we can run algorith to find strongly connected components  
print('for the below type 1 or 2 depending on if you prefer the first or second option')
for i in combins:
    answer = False
    while not answer:
        pref = input(f'{i[0]}, or, {i[1]}')
        try:
            if int(pref) == 1:
                directed_edges.append((i[0],i[1]))
                answer = True
            elif int(pref) == 2:
                directed_edges.append((i[1],i[0]))
                answer = True
        except:
            continue

# elements of this list are sets of strongly connected components 
        
G_SSC = nx.DiGraph(directed_edges)
connected_nodes = [x for x in nx.kosaraju_strongly_connected_components(G_SSC) if len(x) > 1]

#finds cycles in graph and creates set of edges to represent those cycles
Gr = nx.DiGraph(directed_edges)
cy = list(nx.simple_cycles(Gr))

cycles = []
for i in connected_nodes:
    b = [x for x in cy if all(item in x for item in i) == True]
    cycles.append(b[0])

def nodes_to_edges(node_list): #this is just taking the ouput of nx.simple_cycles from a list to set of tuples
    edges = ()
    for i in range(len(node_list)-1):
        edge = (node_list[i], node_list[i+1])
        edges = edges + (edge,)
        print(edge)
    edges = edges +((node_list[-1], node_list[0]),)
    return edges
        
edge_cycles = []
for i in cycles:
    edge_cycles.append(nodes_to_edges(i))

    
# plots graph of preferences

G = nx.DiGraph()
G.add_edges_from(directed_edges)
node_size = [len(v) * 400 for v in G.nodes()]

# edge colours
colours = ['black','red','blue','green','pink']   
             
d = [[] for x in range(len(edge_cycles)+1)]

def edge_colourer(cycleList, edge):
    for cycle in cycleList:
         
        if edge in cycle:
            return cycleList.index(cycle)+1 
    return 0

for edge in directed_edges:
    placement = edge_colourer(edge_cycles, edge)
    if placement>4:
        placement = 1
    d[placement].append(edge)
    

#type of layout
plt.figure(figsize=(9,9))
pos = nx.circular_layout(G)
#edges
for i in range(len(d)):
    nx.draw_networkx_edges(G, pos, edgelist=d[i], edge_color=colours[i], alpha = 0.6, 
                       node_size=node_size, width=2, arrows=True, arrowsize=40)

#nodes
nx.draw_networkx_nodes(G, pos, node_size = node_size, node_color="Grey")

#labels
nx.draw_networkx_labels(G, pos)
#graph
plt.axis("off")
plt.show()



