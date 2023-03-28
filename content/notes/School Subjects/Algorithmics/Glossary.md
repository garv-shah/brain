---
title: "Glossary"
cards-deck: notes::School Subjects::Algorithmics
---
#algo 

## How do you notate a graph? #card
A **graph $G=(V,E)$** is a set of vertices $V(G)$, a set of edges $E(G)$, and a relation that associates two vertices via an edge.
^1678270591198

## Adjacent Nodes #card
Two vertices $v$ and $w$ in graph $G$ are **adjacent**, denoted $v-w$, if there is an edge between them.
^1678270591202

## Incident #card 
If the vertex v is an endpoint of the edge e, then e and v are **incident**.
^1678270591203

## Degree #card 
The **degree** d(v) of a vertex v is the number of edges incident to it, counting loops twice.
^1678270591204

## Path #card 
A path is a trail in which neither vertices nor edges are repeated. A path is also a trail, thus it is also an open walk. 
![](https://media.geeksforgeeks.org/wp-content/uploads/Untitled-drawing-2-2.png)
Here 6->8->3->1->2->4 is a Path
^1678270591205

## Complete Graph #card 
The **complete graph** is the graph ('$n$' vertices) in which every pair of vertices are adjacent.
Since each node is connected to every other node by an edge, each node has a degree of $n-1$ and there are $\frac{n(n-1)}{2}$ edges.
![[notes/School Subjects/Algorithmics/Diagrams/Connected Graph.png]]
^1678270591206

## Bipartite Graphs #card 
A bipartite graph, also called a bigraph, is a set of graph vertices decomposed into two disjoint sets such that no two graph vertices within the same set are adjacent.
![Bipartite graph - Wikipedia](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Simple_bipartite_graph%3B_two_layers.svg/640px-Simple_bipartite_graph%3B_two_layers.svg.png)
This graph is bipartite because none of the red nodes connect to other nodes.
^1678270591207

## Adjacency Matrix #card 
The **adjacency matrix** $A$ of a graph G with $n$ vertices is the $n\times n$ matrix with rows and columns indexed by the vertices of $G$, where the number in the $i^{th}$ row and $j^{th}$ column of $A$ is the number of edges between the $i^{th}$ and $j^{th}$ vertex, counting loops twice.
![AdjacencyMatrix](https://mathworld.wolfram.com/images/eps-svg/AdjacencyMatrix_1002.svg)
^1678270591208

## Walk #card 
A **walk** is going from any node to another node, and is the most general definition of this process for a graph.
![[notes/School Subjects/Algorithmics/Diagrams/Walk Diagram.png]]
^1678327509204

## Trail #card 
A **trail** is a walk with no repeated edge.
^1678270591209

## Oath #card 
A **oath** is a walk with no repeated vertex.
^1678270591210

## Circuit #card 
A **circuit** is a trail whose first and last vertices are the same.
^1678270591211

## Cycle #card 
A **cycle** is a circuit with no repeated vertex other than the first and last vertex.
![[notes/School Subjects/Algorithmics/Diagrams/Cycle Diagram.png]]
^1678270591212

## Length #card 
The length of a walk, trail, path, circuit, or cycle in a graph is the number of edges in it (counting repeated edges multiple times).
^1678270591213

## Connected #card 
A graph G is **connected** if, for every pair of vertices in G, there exists a path between them.
^1678270591214

## Subgraph #card 
A **subgraph** H of a graph G is a graph such that V (H) is a subset of V (G) and E(H) is a subset of E(G).
^1678270591215

## Eulerian Circuit #card 
A **Eulerian circuit** of a graph G is a circuit which contains every edge of G.
^1678270591216

## Hamiltonian Cycle #card 
A **Hamiltonian cycle** of a graph G is a cycle which contains every vertex of G.
^1678270591217

## Neighbourhood #card 
The **neighbourhood** of a vertex v is the set of vertices adjacent to v.
^1678270591218

## Tree #card 
A **tree** is a connected graph with no cycles.
![[notes/School Subjects/Algorithmics/Diagrams/Tree Diagram.png]]
^1678270591219

## Leaf #card 
A **leaf** of a tree is a vertex of degree 1.
^1678270591220

## Spanning Subgraph #card
A subgraph that is obtained only by edge deletions, so it therefore contains all the vertices of the original graph.
^1678270591221

## Distance #card 
The **distance** between two vertices v and w is the length of the shortest path between them.
^1678327509207

## Forest #card 
A **forest** is a graph with no cycles. (and it only wouldn't be connected if there are multiple trees within the forest)
^1678327509208

## Diameter #card 
The longest shortest path from any node to another. This means that is the maximum distance to get from any node to another.
![](https://media.geeksforgeeks.org/wp-content/uploads/g1.jpg.jpg)
The diameter here would be 3!
^1678327509209

## Radius #card
The radius of a graph is the minimum distance you can take to get to any other node from a central node. For example, in this graph, C can get to any other node in 2 moves, so the radius would be 2.
![[notes/School Subjects/Algorithmics/Diagrams/Radius Diagram.png]]
^1678327509210

## Eccentricity #card
The eccentricity is of a vertex is the maximum distance between the vertex and any other vertex. Below is a graph with each node labelled with its eccentricity.
![enter image description here](https://i.stack.imgur.com/rHkBT.png)
^1678327509211

## Digraph #card 
A directed graph, or digraph, is a graph where each edge has a direction.
![](https://media.geeksforgeeks.org/wp-content/uploads/20200630114438/directed.jpg)
A digraph is strongly connected if there is a directed path from every vertex to every other vertex in the graph.
^1678327509212

## DAGs #card 
A directed graph that is acyclic (contains no cycles) is known as a DAG. All trees are DAGs with the added restriction that each child only has one parent.
^1678327509213
