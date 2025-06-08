from collections import deque

# ---------- BFS using Edge List ----------
def bfs_edge_list(edges, start, num_vertices):
    """
    BFS implementation for a graph represented as an edge list.
    edges: list of tuples (source, destination) representing directed edges.
    start: starting vertex.
    num_vertices: total number of vertices in the graph.
    """
    visited = [False] * num_vertices
    order = []
    queue = deque([start])
    visited[start] = True

    while queue:
        current = queue.popleft()
        order.append(current)
        # For every edge, if the current vertex is the source, add the destination.
        for u, v in edges:
            if u == current and not visited[v]:
                visited[v] = True
                queue.append(v)
    return order

# ---------- BFS using Adjacency List ----------
def bfs_adj_list(adj_list, start):
    """
    BFS implementation for a graph represented as an adjacency list.
    adj_list: dictionary where each key is a vertex and the value is a list of neighboring vertices.
    start: starting vertex.
    """
    visited = set()
    order = []
    queue = deque([start])
    visited.add(start)

    while queue:
        current = queue.popleft()
        order.append(current)
        # Add all unvisited neighbors of the current vertex.
        for neighbor in adj_list.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

# ---------- BFS using Adjacency Matrix ----------
def bfs_adj_matrix(matrix, start):
    """
    BFS implementation for a graph represented as an adjacency matrix.
    matrix: 2D list where matrix[i][j] is non-zero if there's an edge from i to j.
    start: starting vertex.
    """
    n = len(matrix)
    visited = [False] * n
    order = []
    queue = deque([start])
    visited[start] = True

    while queue:
        current = queue.popleft()
        order.append(current)
        # Check every possible vertex as a neighbor.
        for neighbor in range(n):
            # If there is an edge (non-zero weight) and neighbor is not visited.
            if matrix[current][neighbor] != 0 and not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return order

# ---------- Example Graphs ----------

# 1. Edge List (Directed Graph)
# Each tuple is in the format (source, destination)
edges = [(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)]
num_vertices = 4
print("BFS using Edge List:", bfs_edge_list(edges, start=2, num_vertices=num_vertices))

# 2. Adjacency List
# Using a dictionary for clarity.
adj_list = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}
print("BFS using Adjacency List:", bfs_adj_list(adj_list, start=2))

# 3. Adjacency Matrix
# 0 represents no edge, non-zero (here 1) represents an edge.
# This matrix corresponds to the same graph as above.
matrix = [
    [0, 1, 1, 0],  # Vertex 0 has edges to 1 and 2
    [0, 0, 1, 0],  # Vertex 1 has an edge to 2
    [1, 0, 0, 1],  # Vertex 2 has edges to 0 and 3
    [0, 0, 0, 1]   # Vertex 3 has an edge to itself (self-loop)
]
print("BFS using Adjacency Matrix:", bfs_adj_matrix(matrix, start=2))




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
