import networkx as nx
import random

# find the sortest path from a source node to all other nodes in a graph 

def dijkstra_algorithms(graph,start,end):
    size = len(graph)
    table = [100 for _ in range(size)]
    table[start] = 0
    visited = [False for _ in range(size)]
    queue = [start]
    while queue:
        node = queue.pop(0)
        if visited[node]:
            continue
        visited[node] = True
        for neighbor,weight in graph[node]:
            print('neighbor,weight of node: ',neighbor,weight,node)
            queue.append(neighbor)
            print('queue',queue)
            print('table[node]',table[node])
            print('table[neighbor]',table[neighbor])
            print('weight',weight)
            table[neighbor] = min(table[neighbor],table[node]+weight)
    print(table)            
    
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
# if __name__ == '__main__':
#     graph = [[(1,1),(2,4)],[(0,1),(2,2),(3,5)],[(0,4),(1,2),(3,1)],[(1,5),(2,1)]]
#     start = 0
    # end = 3
    

if __name__ == '__main__':
    # graph = [[(1,1),(2,4)],[(0,1),(2,2),(3,5)],[(0,4),(1,2),(3,1)],[(1,5),(2,1)]]
    
    def generate_complex_graph(graph, num_nodes, num_edges):
        for _ in range(num_edges):
            node1 = random.randint(0, num_nodes-1)
            node2 = random.randint(0, num_nodes-1)
            weight = random.randint(1, 10)
            graph[node1].append((node2, weight))
            graph[node2].append((node1, weight))

    num_nodes = 8
    num_edges = 14
    graph = [[] for _ in range(num_nodes)]
    generate_complex_graph(graph, num_nodes, num_edges)
    start = 0
    end = 3
    dijkstra_algorithms(graph, start, end)
    visualize_graph(graph)
    

        