---
title: "Bridge Crossing Problem"
---
#algo #graphtheory 

Four friends need to cross a bridge. They start on the same side of the bridge.

A maximum of two people can cross at any time.

It is night and they have just one lamp. People that cross the bridge must carry the lamp to see the way.

A pair must walk together at the rate of the slower person.

-   Ann takes 1 minute to cross
-   Ben takes 2 minutes to cross
-   Con takes 7 minutes to cross
-   Dora takes 10 minutes to cross

In the forum, collaborate with your classmate:

1.  Represent the model as a graph/digraph or tree.
2.  Describe using Graph Terminology the properties of each model.
   
As you can see from this partial tree diagram (it was too much effort to complete it 😭), the problem can also be modelled similar to events in probability, where every possible action after one action is noted down in a tree like structure.

In this case, the nodes represent a person (or pair) walking across the bridge, and the edges represent the process of crossing the bridge, the number showing the amount of time this takes.

   ```mermaid
graph TB
	A((A: 1))
	B((A: 2))
	C((A: 7))
	D((A: 10))
```

```mermaid
graph LR
    S((Start)) -->|2| A+B -->|1| A1[A]
    S -->|7| A+C -->|1| A2[A]
    S -->|10| A+D -->|1| A3[A]
    S -->|7| B+C -->|2| B1[B]
    S -->|10| B+D -->|2| B2[B]
    S -->|10| C+D -->|7| C1[C]
    
    A1 -->|10| A+D1[A+D] -->|1| A4[A] -->|7| AC[A+C]
    A1 -->|7| A+C1[A+C] -->|1| A5[A] -->|10| AD[A+D]
    
    A2 -->|2| A+B1[A+B] -->|1| A6[A] -->|10| A+D3[A+D]
    A2 -->|10| A+D2[A+D] -->|1| A7[A] -->|2| A+B2[A+B]
    
    A3 -->|2| A+B3[A+B] -->|1| A8[A] -->|7| A+C2[A+C]
    A3 -->|7| A+C3[A+C] -->|1| A9[A] -->|2| A+B4[A+B]
```