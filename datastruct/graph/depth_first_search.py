def dfs(graph,start,visited=set()):
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs(graph,next,visited)
    return visited
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

dfs(graph, 'A')