import networkx as nx
import random

# find the sortest path from a source node to all other nodes in a graph 

def dijkstra_algorithms_with_simple_array(graph,start):
    visited = [False]*len(graph)
    table = [[None,None]]*len(graph)
    table[start] = [0,None]
    queue = [start]
    while queue:
        node = queue.pop(0)
        if visited[node]:
            continue
        visited[node] = True
        distance,previous = table[node]
        if distance is None:
            continue
        for neighbor,weight in graph[node]:
            distance_neighbor,previous_neighbor = table[neighbor]
            print('distance_neighbor: ',distance_neighbor)
            print('previous_neighbor: ',previous_neighbor)
            print('weight: ',weight)
            print('distance: ',distance)
            print('previous: ',previous)
            if distance_neighbor is None:
                distance_neighbor = weight + distance
                previous_neighbor = node
                table[neighbor] = [distance_neighbor,previous_neighbor]
            elif distance_neighbor > weight + distance:
                distance_neighbor = weight + distance
                previous_neighbor = node
                table[neighbor] = [distance_neighbor,previous_neighbor]
            else:
                pass 
            queue.append(neighbor)
        
    return table 
            
import heapq

# This class represents a directed graph using
# adjacency list representation
class Graph:
    def __init__(self, V):
        self.V = V  # No. of vertices
        self.adj = [[] for _ in range(V)]  # In a weighted graph, store vertex and weight pair for every edge

    # Function to add an edge to the graph
    def add_edge(self, u, v, w):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))

    # Prints shortest paths from src to all other vertices
    def shortest_path(self, src):
        # Create a priority queue to store vertices that
        # are being preprocessed.
        pq = [(0, src)]  # The first element of the tuple is the distance, and the second is the vertex label

        # Create a list for distances and initialize all
        # distances as infinite (INF)
        dist = [float('inf')] * self.V
        dist[src] = 0

        # Looping until the priority queue becomes empty
        while pq:
            # The first element in the tuple is the minimum distance vertex
            # Extract it from the priority queue
            current_dist, u = heapq.heappop(pq)

            # Iterate over all adjacent vertices of a vertex
            for v, weight in self.adj[u]:
                # If there is a shorter path to v through u
                if dist[v] > dist[u] + weight:
                    # Update the distance of v
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))

        # Print shortest distances
        print("Vertex Distance from Source")
        for i in range(self.V):
            print(f"{i}\t\t{dist[i]}")



import matplotlib.pyplot as plt

def visualize_graph(graph):
    G = nx.Graph()
    for node, neighbors in enumerate(graph):
        for neighbor, weight in neighbors:
            G.add_edge(node, neighbor, weight=weight)
    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, edge_color='gray')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    plt.show()                
if __name__ == '__main__':
    # graph = [[(1,1),(2,4)],[(0,1),(2,2),(3,5)],[(0,4),(1,2),(3,1)],[(1,5),(2,1)]]
    
    def generate_complex_graph(graph, num_nodes, num_edges):
        # Generate a connected graph with random weights
        for i in range(num_nodes - 1):
            # Connect each node to the next node
            weight = random.randint(1, 10)
            graph[i].append((i + 1, weight))
            graph[i + 1].append((i, weight))
        
        # Add remaining edges randomly
        while len(get_all_edges(graph)) < num_edges:
            node1 = random.randint(0, num_nodes - 1)
            node2 = random.randint(0, num_nodes - 1)
            if node1 != node2 and not is_edge_exists(graph, node1, node2):
                weight = random.randint(1, 10)
                graph[node1].append((node2, weight))
                graph[node2].append((node1, weight))
        
        return graph

    def get_all_edges(graph):
        edges = set()
        for node, neighbors in enumerate(graph):
            for neighbor, _ in neighbors:
                edge = tuple(sorted((node, neighbor)))
                edges.add(edge)
        return edges

    def is_edge_exists(graph, node1, node2):
        for neighbor, _ in graph[node1]:
            if neighbor == node2:
                return True
        return False


    num_nodes = 7
    num_edges = 14
    graph = [[] for _ in range(num_nodes)]
    generate_complex_graph(graph, num_nodes, num_edges)
    print('graph: ',graph)
    start = 0
    end = 3
    table = dijkstra_algorithms(graph, start)
    print('table :',table)
    visualize_graph(graph)
    

        