# EX3


### Authors:
Yuval Ben Yaakov , Ofir Magen  
-----------


## Summary:
-------

## Setup and data structure
the DiGraph is implemented by using 3 dictionaries (1 is containning all the nodes in the graph , 1 for all the exit edges , 1 for all the the entrance edges)

## DiGraph class methods: 
-----
1. v_size – returns the amount of nodes in the graph
2. e_size – returns the amount of edges in the graph
3. get_mc – returns the MC of this graph
4. add_edge – connects an edge between 2 nodes (id1 --> id2) with a given weight 
5. add_node - adds a node to the graph 
6. remove_node - removes a node and the edges tied to him from the graph
7. remove_edge -  removes an edge from the graph (src --> dest)
8. get_all_v – returns a dictionary of all the nodes in the graph
9. all_in_edges_of_node – returns a dictionary of all edges that go into this node
10. all_out_edges_of_node – returns a dictionary of all edges that go from this node

## GraphAlgo class methods: 
-----
1. init - inits a graph that the algorithms performs on O(1)
2. get_graph - returns the graph the algorithms performs on
3. load_from_json - loads a graph from a json file into this class
4. save_to_json - saves a the graph in the class into a json file
5. shortest_path - returns a tuple that the first argument is the shortest distance from src to dest (by weight) and the second argument is the path (by keys)
this method traversing the graph using BFS and marking in a dictionary every node shortest distance and updating if needed after that the method goes back from the dest node to the src and building the path 
6. connected_component - returns the connected componnets to a given node_id this method using connnected components and searching the list that node_id is in
7. connected_components - returns all the strongly connected components in the graph this method uses Tarjan's algorithm with Nuutila modification so it can run iterative instead of recursive
8.plot_graph - draw the graph using matplotlib

