# 6.0002 Problem Set 2
# Graph Optimization
# Name:
# Collaborators:
# Time: 5 minutes

#
# A set of data structures to represent the graphs that you will be using for this pset.
#


class Node(object):
    """Represents a node in the graph"""

    def __init__(self, name):
        self.name = str(name)

    def get_name(self):
        ''' return: the name of the node '''
        return self.name

    def __str__(self):
        ''' return: The name of the node.
                This is the function that is called when print(node) is called.
        '''
        return self.name

    def __repr__(self):
        ''' return: The name of the node.
                Formal string representation of the node
        '''
        return self.name

    def __eq__(self, other):
        ''' returns: True is self == other, false otherwise
                 This is function called when you used the "==" operator on nodes
        '''
        if not isinstance(other, Node):
            return False
        return self.name == other.name

    def __ne__(self, other):
        ''' returns: True is self != other, false otherwise
                This is function called when you used the "!=" operator on nodes
        '''
        return not self.__eq__(other)

    def __hash__(self):
        ''' This function is necessary so that Nodes can be used as
        keys in a dictionary, Nodes are immutable
        '''
        return self.name.__hash__()


# PROBLEM 1: Implement this class based on the given docstring.
class DirectedRoad(object):
    """Represents a road (edge) with an integer time (weight)"""

    def __init__(self, src, dest, total_time, road_type):
        """ Initialize  src, dest, total_time, and road_type for the DirectedRoad class
            src: Node representing the source node
            dest: Node representing the destination node
            total_time: int representing the time travelled between the src and dest
            road_type: string representing the type of road of the edge
        """
        pass

    def get_source(self):
        """ Getter method for DirectedRoad
            returns: Node representing the source node """
        pass

    def get_destination(self):
        """ Getter method for DirectedRoad
            returns: Node representing the destination node """
        pass

    def get_type(self):
        """ Getter method for DirectedRoad
            returns: String representing the road type of the road"""
        pass

    def get_total_time(self):
        """ Getter method for DirectedRoad
            returns: int representing the time travelled between the source and dest nodes"""
        pass

    def __str__(self):
        """ to string method
            returns: string with the format 'src -> dest takes total_time hours via road_type road' """
        pass

# PROBLEM 1: Implement methods of this class based on the given docstring.
# DO NOT CHANGE THE FUNCTIONS THAT HAVE BEEN IMPLEMENTED FOR YOU.
class RoadMap(object):
    """Represents a road map -> a directed graph of Node and DirectedRoad objects"""

    def __init__(self):
        self.nodes = set()
        self.roads = {}  # must be a dictionary of Node -> list of roads starting at that node

    def __str__(self):
        road_strs = []
        for roads in self.roads.values():
            for road in roads:
                road_strs.append(str(road))
        road_strs = sorted(road_strs)  # sort alphabetically
        return '\n'.join(road_strs)  # concat road_strs with "\n"s between them

    def get_roads_for_node(self, node):
        ''' param: node object
            return: a copy of the list of all of the roads for given node.
                    empty list if the node is not in the graph
        '''
        pass

    def get_all_nodes(self):
        '''returns a COPY of all nodes in the RoadMap. Does not modify self.nodes'''
        return self.nodes.copy()

    def has_node(self, node):
        ''' param: node object
            return: True, if node is in the graph. False, otherwise.
        '''
        pass

    def add_node(self, node):
        """ param: node object
            Adds a Node object to the RoadMap.
            Raises a ValueError if it is already in the graph."""
        pass

    def add_road(self, road):
        """ param: DirectedRoad object
            Adds a DirectedRoad instance to the RoadMap.
            Raises a ValueError if either of the nodes associated with the road is not in the graph."""
        pass
