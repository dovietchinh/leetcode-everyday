from typing import *
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        memory = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    memory[i][j] = grid[i][j]
                elif i == 0 and j>0:
                    memory[i][j] = memory[i][j-1] + grid[i][j]
                elif i > 0 and j == 0:
                    memory[i][j] = memory[i-1][j] + grid[i][j]
                else:
                    memory[i][j] = min(memory[i-1][j],memory[i][j-1])+grid[i][j]
        return memory[m-1][n-1]
            


if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6]]
    r = Solution().minPathSum(matrix)
    print(r)