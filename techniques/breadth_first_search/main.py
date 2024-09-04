# from collections import deque


# import matplotlib.pyplot as plt
# import networkx as nx

# # BFS from given source s
# def bfs(adj, s, visited):
  
#     # Create a queue for BFS
#     q = deque()

#     # Mark the source node as visited and enqueue it
#     visited[s] = True
#     q.append(s)

#     # Iterate over the queue
#     while q:
      
#         # Dequeue a vertex from queue and print it
#         curr = q.popleft()
#         print(curr, end=" ")

#         # Get all adjacent vertices of the dequeued 
#         # vertex. If an adjacent has not been visited, 
#         # mark it visited and enqueue it
#         for x in adj[curr]:
#             if not visited[x]:
#                 visited[x] = True
#                 q.append(x)

# # Function to add an edge to the graph
# def add_edge(adj, u, v):
#     adj[u].append(v)
#     adj[v].append(u)

# # Example usage
# if __name__ == "__main__":
  
#     # Number of vertices in the graph
#     V = 5

#     # Adjacency list representation of the graph
#     adj = [[] for _ in range(V)]

#     graph = {
#         'A': {'B': 4, 'C': 2},
#         'B': {'A': 4, 'C': 5, 'D': 10},
#         'C': {'A': 2, 'B': 5, 'D': 3, 'E': 4},
#         'D': {'B': 10, 'C': 3, 'E': 1, 'F': 5},
#         'E': {'C': 4, 'D': 1, 'F': 2},
#         'F': {'D': 5, 'E': 2, 'G': 3},
#         'G': {'F': 3, 'H': 6},
#         'H': {'G': 6}
#     }
#     adj = [[] for _ in range(len(adj))]
#     # Add edges to the graph
#     add_edge(adj, 0, 1)
#     add_edge(adj, 0, 2)
#     add_edge(adj, 1, 3)
#     add_edge(adj, 1, 4)
#     add_edge(adj, 2, 4)

#     G = nx.DiGraph()
#     for node, edges in graph.items():
#         for neighbor, weight in edges.items():
#             G.add_edge(node, neighbor, weight=1)
#             print('node, neighbor: ',node, neighbor)
#             add_edge(adj, node, neighbor)    
#     pos = nx.spring_layout(G)
#     edge_labels = nx.get_edge_attributes(G, 'weight')
#     nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=16, font_weight='bold', arrows=True)
#     nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=12)

# # Show the plot
#     plt.title("Graph Visualization with Dijkstra's Algorithm")
#     plt.axis('off')
#     plt.show()
#     # Mark all the vertices as not visited
#     visited = [False] * V

#     # Perform BFS traversal starting from vertex 0
#     print("BFS starting from 0: ")
#     bfs(adj, 0, visited)


def bfs(graph, start):
    visited = [] 
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbours = graph[node]
            for neighbour in neighbours:
                queue.append(neighbour)
