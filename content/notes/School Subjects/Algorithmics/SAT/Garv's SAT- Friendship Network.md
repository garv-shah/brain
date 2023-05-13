> How can a tourist best spend their day out?

> [!info]
> I've been finding it hard to plan trips with my friends, especially when everybody lives all over the city and we would all like to travel together. This SAT project aims to model the Victorian public transport network and its proximity to friends' houses, factoring in data about each individual to find the most efficient and effective traversals and pathways for us travelling to locations around Victoria.

I will start and end my day at my house, picking up all my friends along the way. The algorithm will find the quickest route to go to all my friends' houses, go to our desired location(s), and drop them all off before I go back to my own house. It will then return to me the traversal path, the time taken, and my cost for transport throughout the day. 

## Information to Consider
The following is key information to consider when modelling the real life problem. This will be done by representing the problem with an undirected network/graph, as all public transport methods go both ways, just at different times depending on the transport method.

### Node Representation
Nodes represent key landmarks such as train stations, bus stops or a tourist attraction.

### Edge Representation
Edges represent a route (train, bus, tram, walking, etc) from one location to another

### Weight Representation
The edge weights will represent:
- the time taken to travel from one house to the other
- the financial cost of the route, with buses being more expensive than trains, which are more expensive than walking, etc.
These can be interchanged to prioritise the certain attribute, such as time or money being of higher importance in the algorithm.

### Additional Information Modelled Outside Graph
The following would be modelled as dictionaries:
- The arrival time/timetable of buses and trains
- The cost of changing lines
- Attributes of each friend, such as name, home, the time they wake up, the amount of time they take to get ready, and who is friends with whom or to what degree.
- Proximity to all friends' houses (by walking), which would be a dictionary for each node separately. 
This information could be used to add further complications to make the model reflect real life more closely, such as different friends being ready earlier than others or requiring a certain number of "close friends" (by threshold) to be within the travel party at all times.

## Abstract Data Types
I have selected a number of stations, bus stops and locations which I feel are relevant to my friend group.

| Property                     | Stored as                                                    | Notes                                                                                                                                                                 |
| ---------------------------- | ------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Key Landmarks                | Node                                                         |                                                                                                                                                                       |
| Landmark Name                | Node Attribute                                               |                                                                                                                                                                       |
| Route                        | Edge                                                         |                                                                                                                                                                       |
| Route Name                   | Edge Attribute                                               |                                                                                                                                                                       |
| Transport Method/Line        | Edge Colour                                                  |                                                                                                                                                                       |
| Time or Cost                 | Edge Weight                                                  | These can be interchanged to prioritise different aspects. Distance is more relevant than time, but cost may be important as well.                                    |
| Time/Cost of Changing Lines  | Node attribute "interchange_cost" & "interchange_time"       |                                                                                                                                                                       |
| Train and Bus Timetable      | Dictionary: Dict<String: Array<Dict<String: Int or String>>> | Keys would be each line (bus or train), and the values would be arrays of dictionaries with what node they are at, arrival times and departure times.                 |
| Attributes of Each Friend    | Dictionary: Dict<String: Dynamic>                            | This will be a json style nested dictionary that has various attributes about each friend, such as waking up time, other close friends and other relevant information |
| Proximity to Friends' Houses | Node Attribute: Dict<String: Float>                          | Proximity of all houses as an attribute for each node, which has keys as friends' names and values as the distance or time to their house                                     |
## Possible Graph
![[notes/Attachments/Algorithmics/Possible Friendship Network.png]]

## Signatures
| Function Name    | Signature                                                  |
| ---------------- | ---------------------------------------------------------- |
| addLandmark      | \[name, interchange_cost, friend_proximity] -> node        |
| addRoute         | \[start_node, end_node, travel_method, time, cost] -> edge |
| findShortestPath | \[start_node, end_node] -> integer, array                  |
| addFriend                 | \[name, wake_time, close_friends] -> dictionary                                                          |

## Algorithm Selection
While simplifying my problem, I found that starting and ending my day at my house while picking up all my friends along the way is simply an applied version of finding the shortest hamiltonian circuit. In other words, the shortest cost circuit that will visit every node.

While researching into how to solve this, I found that this was a classic example of the travelling salesman problem, which turns out to be an NP-hard problem. This means that there currently exists no exact solution to the problem in polynomial time, and the best I can currently do is the Held–Karp algorithm, which has a time complexity of $O(n^{2}2^{n})$ which is not ideal at all in terms of efficiency, but will have to be sufficient for the use cases of this project.

### Held-Karp algorithm
The Held-Karp algorithm is a method for finding the exact shortest hamiltonian circuit in the exponential time complexity of $O(n^{2}2^{n})$, which is much better than if we to brute force it, which would have a complexity of $O(n!)$. 