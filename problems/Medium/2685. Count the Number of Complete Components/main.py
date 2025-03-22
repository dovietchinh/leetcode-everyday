from collections import defaultdict
from typing import *
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        #handle basic case
        if n == 1:
            return 1
        if len(edges) == 0:
            return n
        count = 0 
        visited = set()
        adj_list = defaultdict(list)
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        def bfs(start):
            nonlocal visited
            if start in visited:
                return False
            queue = [start]
            visited2 = {}
            count_node_in_subgraph = 0
            while queue:
                node = queue.pop(0)
                if node in visited2:
                    continue 
                visited2[node] = 0
                count_node_in_subgraph += 1
                for i in adj_list[node]:
                    queue.append(i)
                    visited2[node] += 1
            connected = True 
            for i in visited2:
                visited.add(i)
                if visited2[i] != count_node_in_subgraph -1:
                    connected = False 
            return connected
        for i in range(n):
            if bfs(i):
                count += 1
        return count 

if __name__ == '__main__':
    n = 4
    edges =  [[1,0],[2,1],[3,0],[3,2]]
    r = Solution().countCompleteComponents(n,edges)
    print('r: ',r)

# BFS for each node in graph
# each BFS go though all node in a subgraph 
# if a subgraph is connected-components : 
#   each node have m -1 edges