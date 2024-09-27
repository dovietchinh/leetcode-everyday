from typing import *
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #backtracking 
        table = [[0 for _ in range(n)] for _ in range(m)]
        def dp(i,j):
            # print(i,j)
            nonlocal table
            if i < 0 or j < 0:
                return 0
            if table[i][j] != 0:
                return table[i][j]
            if i == 0 and j == 0:
                table[i][j] = 1
                return 1
            table[i][j] = dp(i-1,j) + dp(i,j-1)
            return table[i][j]
        return dp(m-1,n-1)
        # return table[m-1][n-1]



if __name__ == '__main__':
    r = Solution().uniquePaths(3,7)
    print('result->', r)