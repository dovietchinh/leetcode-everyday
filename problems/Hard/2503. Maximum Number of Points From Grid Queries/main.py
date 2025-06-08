from typing import *
import heapq
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        def bfs(start):
            queue = [(grid[0][0],start)]
            visited = set()
            table = [[None for _ in range(n)] for _ in range(m)]
            table[0][0] = grid[0][0]
            while queue:
                distance,node = heapq.heappop(queue)
                if node in visited:
                    continue
                visited.add(node)
                # print('node: ',node)
                # print('table:')
                # for ss in table:
                #     print(ss)
                i,j = node
                if i>0:
                    # up i-1,j
                    # distance with path from this node -> neighbor 
                    a = max(distance,grid[i-1][j])
                    if table[i-1][j] is None or a < table[i-1][j]:
                        table[i-1][j] = a
                    heapq.heappush(queue,(a,(i-1,j)))
                if i < m-1:
                    # down i+1,j
                    # distance with path from this node -> neighbor 
                    a = max(distance,grid[i+1][j])
                    if table[i+1][j] is None or a < table[i+1][j]:
                        table[i+1][j] = a
                    heapq.heappush(queue,(a,(i+1,j)))
                if j < n-1:
                    # go right
                    a = max(distance,grid[i][j+1])
                    if table[i][j+1] is None or a < table[i][j+1]:
                        table[i][j+1] = a
                    heapq.heappush(queue,(a,(i,j+1)))
                if j >0:
                    # go left
                    a = max(distance,grid[i][j-1])
                    if table[i][j-1] is None or  a < table[i][j-1]:
                        table[i][j-1] = a
                    heapq.heappush(queue,(a,(i,j-1)))
            return table
        table = bfs((0,0))
        results = []
        for query in queries:
            count = 0
            for i in range(m):
                for j in range(n):
                    if table[i][j] < query:
                        count += 1
            results.append(count)
        return results
        # for j in table:
        #     print(j)






#Denote path from 0-0 to i-j is list of value in each node 
#eg: path (0,0) -> (0,1) -> (0,2) -> (1,2)  : [1,2,3,7]
# We define distance from node i-j to node 0-0 is the max(path)
#Solution :
    # for each node in grid : find the minimum distance from 0-0 to that node








if __name__ == '__main__':
    # grid = [[1,2,3],[2,5,7],[3,5,1]]
    # queries = [5,6,2]
    grid = [[5,2,1],[1,1,2]]
    queries = [3]
    r = Solution().maxPoints(grid,queries)
    print('r: ',r)