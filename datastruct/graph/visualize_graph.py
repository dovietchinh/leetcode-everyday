import matplotlib.pyplot as plt
import networkx as nx

# Define the graph using networkx
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 5, 'D': 10},
    'C': {'A': 2, 'B': 5, 'D': 3, 'E': 4},
    'D': {'B': 10, 'C': 3, 'E': 1, 'F': 5},
    'E': {'C': 4, 'D': 1, 'F': 2},
    'F': {'D': 5, 'E': 2, 'G': 3},
    'G': {'F': 3, 'H': 6},
    'H': {'G': 6}
}

# Create a directed graph
G = nx.DiGraph()

# Add edges to the graph
for node, edges in graph.items():
    for neighbor, weight in edges.items():
        G.add_edge(node, neighbor, weight=weight)

# Define positions of nodes
pos = nx.spring_layout(G)

# Draw the graph
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=16, font_weight='bold', arrows=True)

# Draw edge labels
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=12)

# Show the plot
plt.title("Graph Visualization with Dijkstra's Algorithm")
plt.axis('off')
plt.show()