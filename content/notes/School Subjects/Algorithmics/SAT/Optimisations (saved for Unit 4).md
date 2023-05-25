### Caching Held-Karp's Output

The same principle as above can be applied to the Held-Karp algorithm. Although it is a harder task to make Held-Karp iterative, the result of computations can be stored rather than calling `held_karp` every time. As above, this can be done with an intermediary function, `fetch_hk` which only runs `held_karp` if the value hasn't already been stored.

The pseudocode for this process is relatively simple:

```
cached_hk = dictionary of list -> dict

function fetch_hk (
	start: node, 
	end: node,
	visit: set of nodes 
):
	if cached_hk[[start, end, visit]] does not exists:
		cached_hk[[start, end, visit]] = held_karp(start, end, visit)
	return cached_hk[[start, end, visit]]
end function
```

After being implemented in Python, `fetch_hk` resembles the following:

```python
def fetch_hk(start, end, visit):
    key = frozenset([start, end, frozenset(visit)])
    if key not in cached_hk:
        cached_hk[key] = held_karp(start, end, visit)
    return cached_hk[key]
```

#### Performance Improvement

Though this is a somewhat minor change, the improvements are drastic, with the entire hamiltonian circuit being calculated in less than a second. The $n \space \textrm{vs} \space t$ table now looks like this, with an approximate line of best fit of $y \approx a \times b^{x}$ where $a=0.00000544325$ and $b=2.36503$:

| $n$ (no. nodes) | $t$ (execution time in seconds, 4dp) | $y$ (line of best fit, 4dp) |
|-----------------|--------------------------------------|-----------------------------|
| 0               | 0.0001                               | 0.0000                      |
| 1               | 0.0001                               | 0.0000                      |
| 2               | 0.0001                               | 0.0000                      |
| 3               | 0.0001                               | 0.0001                      |
| 4               | 0.0001                               | 0.0002                      |
| 5               | 0.0002                               | 0.0004                      |
| 6               | 0.0005                               | 0.0010                      |
| 7               | 0.0012                               | 0.0023                      |
| 8               | 0.0030                               | 0.0053                      |
| 9               | 0.0081                               | 0.0126                      |
| 10              | 0.0210                               | 0.0298                      |
| 11              | 0.0520                               | 0.0705                      |
| 12              | 0.2051                               | 0.1667                      |
| 13              | 0.5061                               | 0.3942                      |
| 14              | 0.8246                               | 0.9323                      |
| 15              | 2.2284                               | 2.2050                      |

Evidently this is significantly better, with Held-Karp at 12 nodes being about 8,533 times faster than without this optimisation. Across a couple tests, the $b$ value of the line of best fit seems to hover around $2.1-2.3$, which indicates that we're nearing the limits of our optimisations. The theoretical average time complexity of Held-Karp is $O(2^{n}n^{2})$, and it is unknown if any algorithm exists to solve TSP in a time complexity of less than base 2. As such, the closer we get to base 2, the more "perfectly" we have optimised our algorithm, and as of now we're pretty close.

// this is saved code to be put back in later (optimisation)
```python
    cached_djk = {}
    cached_hk = {}
    
def fetch_djk(start, end):
    """
    Fetches Dijkstra's Shortest Path Algorithm.

    :param start: start node
    :type start: str

    :param end: end node
    :type end: str

    :return: The shortest distance between two nodes along with the path.
    :rtype: dict[str, float | list[str]]
    """

    global cached_djk
    if start not in cached_djk:
        cached_djk[start] = dijkstra(start)

    djk = cached_djk[start]
    # reconstructs the path
    path = [end]
    while path[0] != start:
        path.insert(0, djk['predecessors'][path[0]])

    return {'cost': djk['distances'][end], 'path': path}

def fetch_hk(start, end, visit):
    key = frozenset([start, end, frozenset(visit)])
    if key not in cached_hk:
        cached_hk[key] = held_karp(start, end, visit)
    return cached_hk[key]
    
def dijkstra(start):
    """
    Dijkstra's Shortest Path Algorithm.

    :param start: start node
    :type start: str

    :return: The distance dictionary and the predecessor dictionary.
    :rtype: dict
    """

    # set all nodes to infinity with no predecessor
    distance = {node: float('inf') for node in g.nodes()}
    predecessor = {node: None for node in g.nodes()}
    unexplored = list(g.nodes())

    distance[start] = 0

    while len(unexplored) > 0:
        min_node = min(unexplored, key=lambda node: distance[node])
        unexplored.remove(min_node)

        for neighbour in g.neighbors(min_node):
            current_dist = distance[min_node] + dist(min_node, neighbour)
            # a shorter path has been found to the neighbour ∴ relax value
            if current_dist < distance[neighbour]:
                distance[neighbour] = current_dist
                predecessor[neighbour] = min_node

    return {'distances': distance, 'predecessors': predecessor}
```
