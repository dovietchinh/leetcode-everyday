import heapq  # Importing the heapq module for a priority queue (min-heap)

def dijkstra_algorithm(graph, start):
    n = len(graph)
    
    # Step 1: Initialize the table (distance, previous node) for all nodes
    table = [[float('inf'), None] for _ in range(n)]  # Distance initialized to infinity, previous node to None
    table[start] = [0, None]  # Starting node has distance 0 and no previous node
    
    # Step 2: Create a priority queue (min-heap) with (distance, node) tuples
    priority_queue = [(0, start)]  # (distance, node)
    heapq.heapify(priority_queue)
    
    visited = [False] * n  # To track visited nodes

    while priority_queue:
        # Step 3: Pop the node with the smallest tentative distance
        current_distance, node = heapq.heappop(priority_queue)
        
        # If the node is already visited, continue
        if visited[node]:
            continue
        visited[node] = True
        
        # Step 4: Explore neighbors of the current node
        for neighbor, weight in graph[node]:
            if visited[neighbor]:
                continue
            
            # Calculate new tentative distance
            new_distance = current_distance + weight
            if new_distance < table[neighbor][0]:  # If new distance is shorter, update
                table[neighbor] = [new_distance, node]
                heapq.heappush(priority_queue, (new_distance, neighbor))
    
    return table

def build_graph(edges, n):
    # Initialize the graph as an adjacency list
    graph = {i: [] for i in range(n)}
    
    # Populate the adjacency list with edges
    for node1, node2, weight in edges:
        graph[node1].append((node2, weight))
        graph[node2].append((node1, weight))  # Since the graph is undirected
    
    return graph

# Example usage:
edges = [
    [3, 0, 4], [0, 2, 3], [1, 2, 2], [4, 1, 3],
    [2, 5, 5], [2, 3, 1], [0, 4, 1], [2, 4, 6], [4, 3, 0.5]
]
num_nodes = 6  # Based on the highest numbered node (0 to 5)

# Build the graph from the edges
graph = build_graph(edges, num_nodes)

start_node = 0  # Starting from node 0
result = dijkstra_algorithm(graph, start_node)

# Print the final result (distances and previous nodes)
for i, (dist, prev) in enumerate(result):
    print(f"Node {i}: Distance = {dist}, Previous = {prev}")