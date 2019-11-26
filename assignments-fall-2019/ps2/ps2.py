# 6.0002 Problem Set 2
# Graph Optimization
# Name:
# Collaborators:
# Time:

#
# Finding shortest paths to drive from home to work on a road network
#


import unittest
from graph import DirectedRoad, Node, RoadMap


# PROBLEM 2: Building the Road Network
#
# PROBLEM 2a: Designing your Graph
#
# What do the graph's nodes represent in this problem? What
# do the graph's edges represent? Where are the times
# represented?
#
# ANSWER:
# 
# 


# PROBLEM 2b: Implementing load_map
def load_map(map_filename):
    """
    Parses the map file and constructs a road map (graph).

    Parameters:
        map_filename : name of the map file

    Assumes:
        Each entry in the map file consists of the following format, separated by tabs:
            From To TotalTime  RoadType
        e.g.
            N0	N1	15	interstate
        This entry would become an edge from 'N0' to 'N1' on an interstate highway with 
        a weight of 15. There should also be another edge from 'N1' to 'N0' on an interstate
        using the same weight.

    Returns:
        a directed road map representing the inputted map
    """
    pass

# PROBLEM 2c: Testing load_map
# Include the lines used to test load_map below, but comment them out


# PROBLEM 3: Finding the Shortest Path using Optimized Search Method
#
# PROBLEM 3a: Objective function
#
# What is the objective function for this problem? What are the constraints?
#
# ANSWER:

# PROBLEM 3b: Implement get_neighbors
def get_neighbors(roadmap, node, restricted_roads):
    """
    Finds the neighbors of a node in a given roadmap, without
    considering roads of type in restricted_roads.

    
    Parameter:
        roadmap: RoadMap
            The graph on which to carry out the search
        node: Node
            node whose neighbors to retrieve
        restricted_roads: list[strings]
            Road Types not under consideration

    Returns:
        list of neighbor nodes
    """
    pass

# PROBLEM 3c: Implement get_best_path
def get_best_path(roadmap, start, end, restricted_roads, to_neighbor = False):
    """
    Finds the shortest path between nodes subject to constraints.

    Parameters:
        roadmap: RoadMap
            The graph on which to carry out the search
        start: Node
            node at which to start
        end: Node
            node at which to end
        restricted_roads: list[strings]
            Road Types not allowed on path
        to_neighbor: boolean
            flag to indicate whether to get shortest path to end or
            shortest path to some neighbor of end 

    Returns:
        A tuple of the form (best_path, best_time).
        The first item is the shortest-path from start to end, represented by
        a list of nodes (Nodes).
        The second item is an integer, the length (time traveled)
        of the best path.

        If there exists no path that satisfies restricted_roads constraints, then return None.
    """

    
    # Write Dijkstra implementation here

    # PROBLEM 4c: Handle the to_neighbor = True case here

    pass


# PROBLEM 4a: Implement best_path_ideal_traffic
def best_path_ideal_traffic(filename, start, end):
    """Finds the shortest path from start to end during ideal traffic conditions.

    You must use get_best_path and load_map.

    Parameters:
        filename: name of the map file that contains the graph on which
            carry out the search
        start: Node
            node at which to start
        end: Node
            node at which to end
    Returns:
        The shortest path from start to end in normal traffic,
            represented by a list of nodes (Nodes).

        If there exists no path, then return None.
    """
    pass


# PROBLEM 4b: Implement best_path_restricted
def best_path_restricted(filename, start, end):
    """Finds the shortest path from start to end when local roads cannot be used.

    You must use get_best_path and load_map.

    Parameters:
        filename: name of the map file that contains the graph on which
            carry out the search
        start: Node
            node at which to start
        end: Node
            node at which to end
    Returns:
        The shortest path from start to end given the aforementioned conditions,
            represented by a list of nodes (Nodes).

        If there exists no path that satisfies restricted_roads constraints, then return None.
    """
    pass

# PROBLEM 4c: Implement best_path_to_neighbor_restricted
def best_path_to_neighbor_restricted(filename, start, end):
    """Finds the shortest path from start to some neighbor of end
    when local roads cannot be used.

    You must use get_best_path and load_map.

    Parameters:
        filename: name of the map file that contains the graph on which
            carry out the search
        start: Node
            node at which to start
        end: Node
            node at which to end; you may assume that start != end
    Returns:
        The shortest path from start to some neighbor of end given the
            aforementioned conditions, represented by a list of nodes (Nodes).

        If there exists no path that satisfies restricted_roads constraints, then return None.
    """
    pass

# UNCOMMENT THE FOLLOWING LINES TO DEBUG

##rmap = load_map('road_map.txt')
##
##start = Node('N0')
##end = Node('N9')
##restricted_roads = ['']
##
##print(get_best_path(rmap, start, end, restricted_roads))
