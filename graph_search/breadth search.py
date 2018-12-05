# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.1'
#       jupytext_version: 0.8.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   language_info:
#     codemirror_mode:
#       name: ipython
#       version: 3
#     file_extension: .py
#     mimetype: text/x-python
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#     version: 3.6.5
#   toc:
#     colors:
#       hover_highlight: '#DAA520'
#       navigate_num: '#000000'
#       navigate_text: '#333333'
#       running_highlight: '#FF0000'
#       selected_highlight: '#FFD700'
#       sidebar_border: '#EEEEEE'
#       wrapper_background: '#FFFFFF'
#     moveMenuLeft: true
#     nav_menu:
#       height: 4px
#       width: 254px
#     navigate_menu: true
#     number_sections: true
#     sideBar: true
#     threshold: 4
#     toc_cell: false
#     toc_section_display: block
#     toc_window_display: false
#     widenNotebook: false
# ---

# %% {"ExecuteTime": {"start_time": "2018-10-23T03:12:09.807536Z", "end_time": "2018-10-23T03:12:09.817622Z"}}
import numpy as np

# %% {"ExecuteTime": {"start_time": "2018-10-23T03:12:10.220588Z", "end_time": "2018-10-23T03:12:10.225441Z"}}
import matplotlib.pyplot as plt

# %% {"ExecuteTime": {"start_time": "2018-10-23T03:37:38.377199Z", "end_time": "2018-10-23T03:37:38.386720Z"}}
from collections import OrderedDict,defaultdict

class Graph():

    def __init__(self):
        self.graph = defaultdict(list)
        self.visit = {}
    #@classmethod
    def edge_add(self, u, v):
        self.graph[u].append(v)
        self.visit[u] = False
        self.visit[v] = False



print("hi")
g=Graph()
g.edge_add(0, 1)
g.edge_add(0, 2)
g.edge_add(1, 2)
g.edge_add(2, 0)
g.edge_add(2, 3)
g.edge_add(3, 3)
print(g.__dict__)
print(g.graph[0])

# %% {"ExecuteTime": {"start_time": "2018-10-23T03:59:12.047239Z", "end_time": "2018-10-23T03:59:12.059291Z"}}
g=Graph()
g.edge_add(1, 2)
g.edge_add(1, 3)
g.edge_add(2, 1)
g.edge_add(2, 4)
g.edge_add(3, 1)
g.edge_add(3, 5)
g.edge_add(2, 5)
g.edge_add(6, 4)
g.edge_add(6, 5)
g.edge_add(4, 2)
g.edge_add(4, 5)

g.edge_add(4, 6)
g.edge_add(5, 2)
g.edge_add(5, 3)
g.edge_add(5, 4)
g.edge_add(5, 6)

print(g.__dict__)

# %% {"ExecuteTime": {"start_time": "2018-10-23T03:50:56.236543Z", "end_time": "2018-10-23T03:50:56.242095Z"}}
import ipdb
def bfs(g, start_pt):
    queue = []
    seq = []

    queue.append(start_pt)
    g.visit[start_pt] = True
    while queue:
        p = queue.pop()
        seq.append(p)

        #ipdb.set_trace()
        while g.graph[p]:
            p1 = g.graph[p].pop()
            #ipdb.set_trace()
            if not g.visit[p1]:
                #ipdb.set_trace()
                queue.append(p1)
                g.visit[p1] = True


    return seq

results=bfs(g,1)
print(results)

# %% {"ExecuteTime": {"start_time": "2018-10-23T03:57:55.598796Z", "end_time": "2018-10-23T03:57:55.603398Z"}}
def BFS(g, s):
    queue = [s]
    visited= [False]* len(g.graph)
    while queue:
        s = queue.pop(0)
        print(s, end = " ")
        for i in g.graph[s]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

# %% {"ExecuteTime": {"start_time": "2018-10-23T03:57:56.352611Z", "end_time": "2018-10-23T03:57:56.376036Z"}}
BFS(g,1)

# %% {"ExecuteTime": {"start_time": "2018-10-23T03:59:02.422583Z", "end_time": "2018-10-23T03:59:02.431374Z"}}
# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
from collections import defaultdict

# This class represents a directed graph
# using adjacency list representation
class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

    # Function to print a BFS of graph
    def BFS(self, s):

        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print (s, end = " ")

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


# %% {"ExecuteTime": {"start_time": "2018-10-23T03:59:25.686094Z", "end_time": "2018-10-23T03:59:25.697863Z"}}
g.BFS(1)

# %%
