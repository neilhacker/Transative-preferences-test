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


options = ['tulum', 'tokyo', 'venice', 'rome','NYC', 'cape town','sydney','wales']

x = itertools.combinations(options,2)

combins = []
for i in x:
    combins.append(i)
random.shuffle(combins)
random.shuffle(combins)
    
        
#This class represents a directed graph using adjacency list representation 
# https://www.geeksforgeeks.org/find-if-there-is-a-path-between-two-vertices-in-a-given-graph/
class Graph: 
   
    def __init__(self,vertices): 
        self.V= vertices #No. of vertices 
        self.graph = defaultdict(list) # default dictionary to store graph 
   
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
   
    # A function used by DFS 
    def DFSUtil(self,v,visited,cycles):
        # Mark the current node as visited and print it 
        visited[v]= True
        #print(v, )
        print(options[v],)
        cycles.append(options[v])
        #Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]: 
            if visited[i]==False: 
                self.DFSUtil(i,visited,cycles)   
  
    def fillOrder(self,v,visited, stack): 
        # Mark the current node as visited  
        visited[v]= True
        #Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]: 
            if visited[i]==False: 
                self.fillOrder(i, visited, stack) 
        stack = stack.append(v) 
      
  
    # Function that returns reverse (or transpose) of this graph 
    def getTranspose(self): 
        g = Graph(self.V) 
  
        # Recur for all the vertices adjacent to this vertex 
        for i in self.graph: 
            for j in self.graph[i]: 
                g.addEdge(j,i) 
        return g 

    # The main function that finds and prints all strongly 
    # connected components 
    def printSCCs(self): 
          
        stack = [] 
        # Mark all the vertices as not visited (For first DFS) 
        visited =[False]*(self.V) 
        # Fill vertices in stack according to their finishing 
        # times 
        for i in range(self.V): 
            if visited[i]==False: 
                self.fillOrder(i, visited, stack) 
  
        # Create a reversed graph 
        gr = self.getTranspose() 
           
         # Mark all the vertices as not visited (For second DFS) 
        visited =[False]*(self.V) 
        
         # Now process all vertices in order defined by Stack 
        cycles = []
        
        while stack: 
            i = stack.pop() 
            if visited[i]==False: 
               gr.DFSUtil(i, visited,cycles)
               print("" )
               cycles.append("")
        return cycles



directed_edges = [] #use this to draw directed graph

g = Graph(len(options)) 

# gets user to rank pairs of options and then updates directed edges for graph later
# and also g so we can run algorith to find strongly connected components  
print('for the below type 1 or 2 depending on if you prefer the first or second option')
for i in combins:
    answer = False
    while not answer:
        pref = input(print(i[0], 'or', i[1]))
        try:
            if int(pref) == 1:
                g.addEdge(options.index(i[0]),options.index(i[1]))
                directed_edges.append((i[0],i[1]))
                answer = True
            elif int(pref) == 2:
                g.addEdge(options.index(i[1]),options.index(i[0]))
                directed_edges.append((i[1],i[0]))
                answer = True
        except:
            continue

# spits out list of nodes, those that are together form strongly connected component 
print ("Following are strongly connected components " +
                           "in given graph") 
cyc = g.printSCCs() 
        
# takes output of cyc and turns it into useful list with sublists of strongly connected nodes
def completeCycles(cycleList):
    allcycles = []
    currentcycle = []
    for i in range(len(cycleList)):
        if cycleList[i] == "":
            if len(currentcycle) > 1:
                allcycles.append(currentcycle)
            currentcycle = []
        else:
            currentcycle.append(cycleList[i])
    return allcycles
        

connected_nodes = completeCycles(cyc)

# this will take the groups of connected nodes, create a list of directed edges that
# only contains those nodes, and then find a set of directed edges that creates a cycle

def equal_node_check(perm, connected_nodes):
    occurances = {}
    for nodez in connected_nodes:
        occurances[nodez] = 0
    for point in perm:
        for elem in point:
            occurances[elem] += 1
            if occurances[elem] > 2:
                return False
    return True

edge_cycles = []
for i in connected_nodes:
    nodes_not_in_cycle = [x for x in options if x not in i]
    edges = [x for x in directed_edges if any(node in x for node in nodes_not_in_cycle) == False] #edges in graph that only contain nodes in cycle
    
    edge_perms = itertools.permutations(edges,len(i))
    
    for perm in edge_perms:
        count = 0
        for num in range(len(perm)-1):
            if perm[num][1]==perm[num+1][0]:
                count+=1
            else:
                break
        if count == len(perm)-1:
            if perm[-1][1] == perm[0][0]:
                if equal_node_check(perm,i) == True:
                    edge_cycles.append(perm)
                    break
 
    
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



