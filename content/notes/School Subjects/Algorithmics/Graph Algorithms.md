---
title: "Graph Algorithms"
cards-deck: notes::School Subjects::Algorithmics
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
![[Graph Algorithms.png]]
^1684293406145

## Depth First Search (DFS) #card
DFS is a graph traversal algorithm that chooses any single neighbour node for each discovered node and proceeds searching from it. This produces long branches, because searching from other neighbours is only carried out once a branch has been fully explored.
- Design Pattern: Decrease & Conquer ∵ grows MST by cheapest edge possible that does not make a cycle
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
^1684293406148

## Applications of DFS and BFS #card 
-   DFS and BFS will both give information about whether one node is connected to another via any path in a graph.
-   If the graph **is** connected, BFS will visit all of its nodes.
-   The traversal tree built by BFS represents the shortest paths from the initial vertex to any other for an unweighted graph.
-   DFS is unsuitable for searching shortest paths for unweighted graphs.
^1684293406149

## Graph Colouring #card 
Graph colouring or vertex colouring is the process of colouring a graph such that no adjacent vertices have the same colour. A $k$-colouring of a graph uses $k$ colours, and the chromatic number is the minimum value of $k$ for which a $k$ colouring exists.
Applications are generally to resolve conflicts, where certain objects cannot be next to each other or certain events cannot run at the same time.
These generally end up being **optimal resource allocation** problems.
^1684293406150

## Detecting Cycles #card 
DFS is used to detect cycles! With a small modification to DFS to maintain a list of visited nodes as well as processed nodes, DFS can detect cycles, and if a we visit a node we have already visited, a cycle is detected.
^1684293406151

## Topological Sorting #card 
The DFS order of the processed list is the topological sorting, normally run from a source node. 
One problem that can be solved by divide and conquer is topological sorting. **Topological sorting** is the ordering of information according to its dependencies and is typically represented by a directed graph showing the order of progress for a particular system.
^1684293406152

## Shortest Path in Unweighted Graphs #card 
BFS is used to find the shortest path in unweighted graphs from one node to another. By rippling out in layers from the starting node, it can find the first path to the end node.
^1684293406153

## Spanning Tree #card 
A **spanning tree** is a connected graph that has no circuits or cycles and which includes all the vertices or nodes of a graph.
A **minimum spanning tree** (MST) is a spanning tree for a weighted graph whose edges add up to the smallest possible value.
^1684293406154

## Prim's Algorithm #card 
**Prim's Algorithm** is a greedy algorithm used for finding the MST in weighted undirected graphs.
- Design Pattern: Marks each processed node and reduces problem sizer by one node in each iteration until all nodes processed
**Prim's algorithm in plain English**
1.  Begin at any vertex.
2.  Select the **cheapest** (minimum-weight) edge emanating from the vertex.
3.  Look at edges coming from the vertices selected so far: select the cheapest edge; if the edge forms a circuit, discard it and select the next cheapest.
4.  Repeat until all vertices have been selected.
5.  Double-check by repeating the process with a different starting vertex.
^1684293406155

## Dijkstra's Algorithm #card 
Dijkstra's algorithm finds the shortest path from the starting location to any other location, not just the desired destination. The algorithm works on weighted graphs and weighted digraphs, **where no negative weight cycles exist.** 
Dijkstra's algorithm is a **greedy** algorithm – that is, one that starts at a given source node in a weighted graph and expands all possible paths from this node using the weights on the edges to all the immediate neighbours. It then repeats this process from the cheapest-cost neighbour at this point in the algorithm. 
As it calculates the shortest path, it marks nodes that have been explored and expanded to their immediate neighbours as 'visited' until all the nodes in the graph have been explored, processed, expanded and visited.
When all nodes have been processed, the shortest path from the source node will have been calculated for all the other nodes in the graph.
```
While there are unvisited vertices do
  find the vertex (V) with the smallest distance in the unvisited vertices list
  remove V from the unvisited vertices list
  for each neighbour (N) of vertex V do
    thisDist:=distance to V plus the weight of the edge V-N
    if thisDist < distance to N then
      A shorter path to N has been found
      Update the shortest path to N distance to N := thisDist
      set the shortest path predecessor to N as V
^1684293406156

    End if
  End do
End do
```

## Bellman-Ford Algorithm #card 
Bellman-Ford, like Dijkstra's uses relaxation to find the shortest path, but it can also *detect* that a negative cycle exists. It will not be able to find the shortest path if this cycle exists. This being said, Bellman-Ford *works* on graphs with negative edge weights, but not negative cycles.
**Unlike Dijkstra’s algorithm, the Bellman-Ford algorithm is not greedy and does not use a priority queue to process the edges.**
^1684293406157

## Dijkstra's vs Bellman-Ford vs Floyd-Warshall #card 
- Dijkstra's: shortest path from **one** node to all nodes
- Bellman-Ford: shortest path from **one** node to all nodes, negative edges **allowed**
- Floyd-Warshall's Shortest Path: shortest path between **all** pairs of vertices, negative edges allowed
Negative cycles are not allowed in any of these algorithms, because shortest path doesn't make sense for negative cycles.
^1684293406158
