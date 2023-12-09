---
title: Garv's Algorithmics Summary Sheet
---
## Prim's Algorithm

### Proof of Correctness

> Prove that Prim's Algorithm always generates the MST for any given graph $G$.

#### Base Case
When the algorithm starts, the tree generated must be a subtree of the MST because only one node is in the tree.

#### Inductive Step

Assume that at step $i$, the tree generated is a subtree of the MST. At step $i + 1$, partition the nodes into two sets, those in the tree already as $S$ and those not as $S'$. The edge added must be the shortest between $S$ and $S'$ because any other edge will increase the cost of the MST. This is exactly what Prim's choose and therefore, the tree generated is still a subgraph of the MST.

This assumption holds until all nodes are included in the MST. Thus, by mathematical induction, Prim's algorithm always generates the MST for any given graph $G$.

## Dijkstra's Algorithm

### Pseudocode

```
function reconstruct(pred: dict, x: node):
	path = []
	prev = x
	while prev != null:
		path.add(prev) to front of list
		prev = pred[prev]
	
	return path

Algorithm dijkstras(s: node, x: node, G: graph):
	// s is the source node, x is the destination node
	
	for node n in G:
		dist[n] = inf
		pred[n] = null
		
	dist[u] = 0
	Q = MinPrioQueue based on dist values of nodes
	
	while Q is not empty:
		u = top(Q)
		Q = dequeue(Q)
		
		if u = x:
			return reconstruct(pred, x)
		
		for each unvisited neighbour v of u:
			tempDist = dist[u] + weight(u,v)
			if tempDist < dist[v]:
				dist[v] = tempDist
				pred[v] = u
	
	return reconstruct(pred, x)
```

### Proof of Correctness

Let $Q$ be a set of vertices whose shortest distances have been finalised by Dijkstra's and let $s$ be the source node.

> Prove that Dijkstra's Algorithm always finds the shortest path from the node $s$ to every other node for any given graph $G$, provided that $G$ has no negative edge weights.

#### **Base Case**
When the algorithm starts, the distance from the source node to itself is zero, which is the shortest distance possible assuming no negative edge weights. Thus, the algorithm holds for the base case.

#### **Inductive Step**
It must be proved that Dijkstra's holds true for all vertices not $Q$. Consider the step in Dijkstra's algorithm where the node $v$ is added to $Q$ via the edge $(u, v)$ where $u \in Q$.

Assume for the sake of contradiction that a shorter path to $v$ exists via some other path. The path must then take the form $s, \cdots, w, x, \cdots, v$, where $w$ is in $Q$ and $x$ is not in $Q$. Since there are no negative weights, the cost of the path $x, \cdots, v$ is $\geq 0$. When selecting a vertex to finalise, Dijkstra's selects the non-finalised vertex with the shortest path. As such, $Cost_{s,\cdots,w,x} \geq Cost_{s, \cdots, u, v}$ because the node $v$ is selected by the algorithm via $(u, v)$. Therefore, $Cost_{s, \cdots, w, x} + Cost_{x,\cdots,v} \geq Cost_{s,\cdots,u,v}$ which contradicts the above assumption that a shorter path exists. Hence, Dijkstra's algorithm correctly finds the shortest distance to the node $v$ via the edge $(u, v)$.

Thus, by mathematical induction, Dijkstra's algorithm correctly calculates the shortest distance from the node $s$ to all other nodes in the graph.

## Bellman-Ford Algorithm

### Proof of Correctness

> Prove that the Bellman-Ford Algorithm always finds the shortest path from the node $s$ to every other node for any given graph $G$, provided that $G$ has no negative cycles.

#### Base Case
At the start this must be true, because only the node $s$ is marked as 0 distance.

#### Inductive Step
Assume that at step $i$, the shortest path from $s$ to any node $n$ steps away are correct. At the step $i + 1$, all edges are checked to see if it can improve the shortest path distance to any node. Therefore, at the end of iteration, all shortest paths of length $i + 1$ are correct.

Thus, by mathematical induction, the shortest path distance to all nodes are correctly stored by the step $|V| - 1$ and above, and hence Bellman-Ford correctly finds the shortest path distances.

## Floyd-Warshall Algorithm

### Pseudocode

```
Algorithm floydWarshall(G: graph):
	V = number of vertices in graph G
	dist = V * V array of minimum distances
	for each vertex v
		dist[v][v] = 0
	for each edge (u,v):
		dist[u][v] = weight(u,v)
	for k from 1 to V:
		for i from 1 to V:
			for j from 1 to V:
				if dist[i][j] > dist[i][k] + dist[k][j]:
					dist[i][j] = dist[i][k] + dist[k][j]
	return dist
```

## 0/1 Knapsack Problem

### Pseudocode

```
Algorithm knapsack(P: list, W: list, m: int, n: int):
	// P is an array of profits e.g. [2, 3, 6, 9] for n = 4
	// m is the capacity and n is the number of items
	add 0 to the front of P and W
	V = n + 1 by m + 1 matrix
	
	for i from 0 to n:
		for w from 0 to m:
			if i = 0 or m = 0:
				V[i, w] = 0
			else:
				V[i, w] = max(V[i - 1, w], V[i - 1, w - W[i]] + P[i])
	
	return max(V)
```

If the items to keep are to be returned, replace `return max(V)` with the following:

```
i = n and j = m
keep = list of 0s of length n + 1
while i>0 and j>0:
	if V[i, j] = V[i - 1, j]:
		// don't keep the item
		keep[i] = 0
		i = i - 1
	else:
		// keep the item
		keep[i] = 1
		i = i - 1
		j = j - W[i]

remove first element from keep
return keep
```

## Change-Making Problem

### Pseudocode

```
Algorithm changeMaker(amount: int, coins: list):
	let dp be array of size amount + 1
	dp[0] = 0
	for a from 1 to amount:
		dp[a] = inf
		for c in coins:
			if a-c >= 0:
				dp[a] = min(dp[a], dp[a-c] + 1)
	if dp[amount] != inf:
		return dp[amount]
	else:
		return -1
```

## Fibonacci

### Pseudocode

```
Algorithm fibonacci(n: int):
	fib = [1, 1]
	for i from 2 to n:
		fib[i] = fib[i-1] + fib[i-1]
	return fib[n]
```

## Quicksort

### Pseudocode

```
Algorithm quicksort(L: array<int>, a: int, b: int):
	P = L[b]
	i = a - 1
	for j from a to b - 1:
		if L[j] < P:
		i = i + 1
		Swap L[i] and L[j]
	Swap L[b] and L[i + 1]
	quicksort(L, a, i)
	quicksort(L, i + 2, b)
```

## Mergesort

### Pseudocode

```
Algorithm mergesort(a: array):
	let n be the side of a
	if n = 1:
		return a
	
	m = n // 2
	
	arr1 = a from 0 to m
	arr2 = a from m + 1 to n
	
	arr1 = mergesort(a)
	arr2 = mergesort(b)
	
	merge = []
	
	while arr1 and arr2 both have elements:
		if arr1[0] > arr2[0]:
			merge.append(arr2[0])
			remove first element from arr2
		else:
			merge.append(arr1[0])
			remove first element from arr1
	
	if arr1 is empty:
		add the rest of arr2 to the end of merge
	else:
		add the rest of arr1 to the end of merge
	
	return merge
```