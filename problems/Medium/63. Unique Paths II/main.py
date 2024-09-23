from typing import *
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        count = 0    
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        memory  =[[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    memory[i][j] = 0
                elif i==0 and j==0:
                    memory[i][j] = 1
                elif i==0:
                    memory[i][j] = memory[i][j-1]
                elif j==0:
                    memory[i][j] = memory[i-1][j]
                else:
                    memory[i][j] = memory[i-1][j] + memory[i][j-1]

        return memory[m-1][n-1]

            

            


if __name__ == '__main__':
    matrix = [[0,1],[0,0]]
    r = Solution().uniquePathsWithObstacles(matrix)
    print(r)