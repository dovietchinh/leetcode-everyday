def dfs_for_adjacency_list():
    graph = {
        'A': {'B', 'C'},      
        'B': {'A', 'D', 'E'},
        'C': {'A', 'F'},
        'D': {'B'},
        'E': {'B', 'F'},
        'F': {'C', 'E'}
    }
    def dfs(graph,node,visited=set()):
        if node in visited:
            return 
        print('node:',node)
        for neighbor in graph[node]:
            visited.add(node)
            dfs(graph,neighbor,visited)
    dfs(graph, 'A')

def dfs_for_edge_list():
    graph = [[0,1],[0,2],[1,3],[1,4],[2,5],[4,5]]
    def dfs(graph,node,visited=set()):
        if node in visited:
            return 
        print('node:',node)
        for edge in graph:
            if edge[0] == node:
                visited.add(node)
                dfs(graph,edge[1],visited)
            elif edge[1] == node:
                visited.add(node)
                dfs(graph,edge[0],visited)
    dfs(graph, 0)

def dfs_for_adjaceny_matrix():
    graph = [
        [0, 1, 1, 0, 0, 0],
        [1, 0, 0, 1, 1, 0],
        [1, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1],
        [0, 0, 1, 0, 1, 0]
    ]
    def dfs(graph,node,visited=set()):
        if node in visited:
            return 
        print('node:',node)
        for neighbor in range(len(graph[node])):
            if graph[node][neighbor] == 1:
                visited.add(node)
                dfs(graph,neighbor,visited)
    dfs(graph, 0)
dfs_for_edge_list()
print()
dfs_for_adjaceny_matrix()