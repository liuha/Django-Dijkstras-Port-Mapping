from collections import defaultdict, deque
import math
from .models import Node, Edge

class Graph(object):
    def __init__(self):
        self.nodes = set() # Nodes models
        self.edges = defaultdict(list) # Edges models
        self.distances = {} 

    # mimic Nodes model
    def add_node(self, value):
        self.nodes.add(value) # Add nodes to graph

    # mimic edges model
    def add_edge(self, from_node, to_node):
        self.edges[from_node].append(to_node) 
        self.edges[to_node].append(from_node)
        x = from_node.x_coord - to_node.x_coord
        y = from_node.y_coord - to_node.y_coord
        distance = math.pow(x, 2) + math.pow(y, 2)
        self.distances[(from_node, to_node)] = math.sqrt(distance)

def dijkstra(graph, initial):
    visited = {initial: 0} # Initial will always be the same
    path = {}  # will be passed to interface

    nodes = set(graph.nodes) # need all nodes that make up the graph

    while nodes: # while condition fails when all nodes are visited
        min_node = None # changes upon certain conditions
        for node in nodes: # each node is looped through from the entire set
            if node in visited: # check if node has already been visited
                if min_node is None: 
                    min_node = node 
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None: 
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            try:
                weight = current_weight + graph.distances[(min_node, edge)]
            except:
                continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path


def shortest_path(graph, origin, destination):
    visited, paths = dijkstra(graph, origin)
    full_path = deque()
    _destination = paths[destination]

    while _destination != origin:
        full_path.appendleft(_destination)
        _destination = paths[_destination]

    full_path.appendleft(origin)
    full_path.append(destination)

    return visited[destination], list(full_path)

def graph_test():
    graph = Graph()

    all_nodes = Node.objects.filter(floor=3)
    #print(all_nodes[1])

    for node in all_nodes:
        graph.add_node(node)

    for node in all_nodes:
        edges = Edge.objects.filter(FromNode=node)
        for edge in edges:
            graph.add_edge(edge.FromNode, edge.ToNode)

    orgin = Node.objects.get(name="3_enter", floor=3)
    destination = Node.objects.get(name="136_o", floor =3)
    path_distance, path_list = shortest_path(graph,orgin, destination)

    return path_list

def get_path(star, end, level):
    graph = Graph()

    all_nodes = Node.objects.filter(floor=level)
    #print(all_nodes[1])

    for node in all_nodes:
        graph.add_node(node)

        edges = Edge.objects.filter(FromNode=node)
        for edge in edges:
            graph.add_edge(edge.FromNode, edge.ToNode)

    orgin = Node.objects.get(name=star, floor=level)
    destination = Node.objects.get(name=end, floor =level)
    path_distance, path_list = shortest_path(graph,orgin, destination)

    return path_list
'''
if __name__ == '__main__':
    graph = Graph()

    all_nodes = Nodes.objects.filter(floor=3)
    #print(all_nodes[1])
    print(all_nodes)

    for node in all_nodes:
        graph.add_node(node)

    
    graph.add_edge('A', 'B', 10)
    graph.add_edge('A', 'C', 20)
    graph.add_edge('B', 'D', 15)
    graph.add_edge('C', 'D', 30)
    graph.add_edge('B', 'E', 50)
    graph.add_edge('D', 'E', 30)
    graph.add_edge('E', 'F', 5)
    graph.add_edge('F', 'G', 2)

    print(shortest_path(graph, 'A', 'D')) # output: (25, ['A', 'B', 'D']) 
'''
