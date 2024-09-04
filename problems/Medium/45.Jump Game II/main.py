from typing import *
class Solution:
    def jump(self, nums: List[int]) -> int:
        ## make graph 
        graph = []
        for i in range(len(nums)):
            adj = [] 
            if nums[i] != 0:
                for j in range(1,nums[i]):
                    adj.append(i+j)
            graph.append(adj)
        # print(graph)

        def bfs(graph,start=0):
            visited = [False] * len(graph)
            queue = [start]
            while queue:
                node = queue.pop(0)
                if visited[node] == False:
                    visited[node] = True
                    # print(node)
                    if(node) == len(graph)-1:
                        return 1
                    queue.extend(graph[node])
        
        bfs(graph)
        return 0


                


        




if __name__ == '__main__':
    n = [2,3,1,1,4]
    # n = [3,2,1]
    # n = [8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]
    r = Solution().jump(n)
    print(r)