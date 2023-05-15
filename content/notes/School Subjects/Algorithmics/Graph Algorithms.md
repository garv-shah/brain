---
title: "Graph Algorithms"
---
#algo 

## Breadth First Search (BFS) #card 
BFS is a graph traversal algorithm that visits all neighbours of a source node, and keeps visiting neighbours of neighbours until the entire graph is traversed.
**BFS algorithm step-by-step**
1.  Add the initial node to the **queue** and mark it as **seen**.
2.  Remove the next element from the **queue** and call it **current**.
3.  Get all neighbours of the **current** node that are not yet marked as **seen**.
4.  Store all these neighbours into the **queue** and mark them all as **seen**.
5.  Repeat steps **2 - 4** until the **queue** becomes empty.
![[notes/Attachments/Graph Algorithms.png]]

## Depth First Search (DFS) #card
DFS is a graph traversal algorithm that chooses any single neighbour node for each discovered node and proceeds searching from it. This produces long branches, because searching from other neighbours is only carried out once a branch has been fully explored.
**DFS algorithm step-by-step**
1.  Add the initial node to the **stack**.
2.  Remove the next element from the **stack** and call it **current**.
3.  If the **current** node was **seen** then skip it (go to step **6**).
4.  Otherwise mark the **current** node as **seen**.
5.  Get all neighbours of the **current** node and add all of them to the **stack**.
6.  Repeat steps **2 - 5** until the **stack** becomes empty.
**Difference from BFS**
-   We use a **stack** instead of the **queue** for storing nodes.
-   Typically we do not check whether a node was **seen** when storing neighbours in the stack – instead we perform this checking when retrieving the node from it.

## Applications of DFS and BFS #card 
-   DFS and BFS will both give information about whether one node is connected to another via any path in a graph.
-   If the graph **is** connected, BFS will visit all of its nodes.
-   The traversal tree built by BFS represents the shortest paths from the initial vertex to any other for an unweighted graph.
-   DFS is unsuitable for searching shortest paths for unweighted graphs.

## Graph Colouring #card 
Graph colouring or vertex colouring is the process of colouring a graph such that no adjacent vertices have the same colour. A $k$-colouring of a graph uses $k$ colours, and the chromatic number is the minimum value of $k$ for which a $k$ colouring exists.
Applications are generally to resolve conflicts, where certain objects cannot be next to each other or certain events cannot run at the same time.
These generally end up being **optimal resource allocation** problems.

## Detecting Cycles #card 
DFS is used to detect cycles! With a small modification to DFS to maintain a list of visited nodes as well as processed nodes, DFS can detect cycles, and if a we visit a node we have already visited, a cycle is detected.

## Topological Sorting #card 
The DFS order of the processed list is the topological sorting, normally run from a source node. 

## Shortest Path in Unweighted Graphs #card 
BFS is used to find the shortest path in unweighted graphs from one node to another. By rippling out in layers from the starting node, it can find the first path to the end node.

## Spanning Tree #card 
A **spanning tree** is a connected graph that has no circuits or cycles and which includes all the vertices or nodes of a graph.
A **minimum spanning tree** (MST) is a spanning tree for a weighted graph whose edges add up to the smallest possible value.

## Prim's Algorithm #card 
**Prim's Algorithm** is a greedy algorithm used for finding the MST in weighted undirected graphs.
**Prim's algorithm in plain English**
1.  Begin at any vertex.
2.  Select the **cheapest** (minimum-weight) edge emanating from the vertex.
3.  Look at edges coming from the vertices selected so far: select the cheapest edge; if the edge forms a circuit, discard it and select the next cheapest.
4.  Repeat until all vertices have been selected.
5.  Double-check by repeating the process with a different starting vertex.