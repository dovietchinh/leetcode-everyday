import networkx as nx
import random
import matplotlib.pyplot as plt

def bfs(graph,start_point):
    visited = [False] * len(graph) 
    queue= [start_point]
    while queue:
        node = queue.pop(0)
        if visited[node] == False:
            visited[node] = True
            ##  do something with the node
            print("node: ",node)
            queue.extend(graph[node])


def generate_random_graph(num_nodes, num_edges):
    graph = nx.Graph()
    graph.add_nodes_from(range(num_nodes))
    for _ in range(num_edges):
        node1 = random.randint(0, num_nodes - 1)
        node2 = random.randint(0, num_nodes - 1)
        graph.add_edge(node1, node2)
    return graph

# Example usage
num_nodes = 10
num_edges = 15
graph = generate_random_graph(num_nodes, num_edges)
bfs(graph, 0)
G = graph
pos = nx.spring_layout(G)
# Draw the graph
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=16, font_weight='bold', arrows=True)

# Draw edge labels
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=12)
plt.show()



    



 