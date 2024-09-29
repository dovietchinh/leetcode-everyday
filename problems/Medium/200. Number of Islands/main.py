from typing import *
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        self.m = len(grid)
        self.n = len(grid[0])
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid,i,j)                  
        return count
    def dfs(self,grid,i,j):
        if i < 0 or j < 0 or i >= self.m or j >= self.n:
            return
        if grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.dfs(grid,i+1,j)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i,j-1)
        
        

        

if __name__ == '__main__':
    board = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    board = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    r = Solution().numIslands(board)
    print('r: ',r)