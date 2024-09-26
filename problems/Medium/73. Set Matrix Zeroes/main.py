from typing import *
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        cols = set()
        rows = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    cols.add(j)
                    rows.add(i)
        for rows in rows:
            matrix[rows] = [0] * n
        for col in cols:
            for i in range(m):
                matrix[i][col] = 0
        
            
        

        
            
                



if __name__ == '__main__':
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    Solution().setZeroes(matrix)
    print(matrix)