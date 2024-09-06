import networkx as nx
import random

# find the sortest path from a source node to all other nodes in a graph 

def dijkstra_algorithms(graph,start):
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
    

        