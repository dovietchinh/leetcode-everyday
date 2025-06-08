from typing import *
import sys
class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        p = list(range(n))
        def find(node):
            parent = p[node]    
            while node!=parent:
                node,parent = parent,p[parent]
            return p[node]

        g = [sys.maxsize for _ in range(n)]
        r = [1 for _ in range(n)]
        def union(n1,n2,weight):
            p1, p2 = find(n1), find(n2)
            g[p1] = g[p2] = (g[p1] & g[p2] & weight)
            if p1 == p2:
                return False 
            if r[p1] >= r[p2]:
                r[p1] += r[p2]
                p[p2] = p1 
            else:
                r[p2] += r[p1]
                p[p1] = p2 
            return True 
        
        for u,v,w in edges:
            print('p: ',p)
            print('u,v: ',u,v)
            print('r: ',r)
            union(u,v,w)
            
        # print(p)
        p1, p2 = find(4), find(2)
        print('p1: ',p1)
        print('p2: ',p2)
        print(g)

if __name__ == '__main__':
    n = 5
    edges = [[0,1,7],[1,3,7],[1,2,1]]
    query = [[0,3],[3,4]]
    r = Solution().minimumCost(n,edges,query)
    # print('r: ',r)
            


