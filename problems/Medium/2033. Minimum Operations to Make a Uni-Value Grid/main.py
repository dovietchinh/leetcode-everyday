from typing import *
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m = len(grid)
        n = len(grid[0])
        if m==1 and n==1:
            return 0
        sum = 0
        arr = []
        for i in range(m):
            for j in range(n):
                arr.append(grid[m][n])
        arr.sort()
        median = arr[m*n//2]
        count = 0
        for i in arr:
            diff = abs(i-median)
            if diff %x !=0:
                return -1 
            count += diff /x
        return int(count)

        


if __name__ == '__main__':
    x = 73
    grid = [[931,128],[639,712]]  # 12 
    x = 2
    grid = [[2,4],[6,8]]
    # x = 1
    # grid = [[1,5],[2,3]]
    # x = 2
    # grid = [[1,2],[3,4]]

    # x = 92
    # grid = [[529,529,989],[989,529,345],[989,805,69]]
    
    r = Solution().minOperations(grid,x)
    print('r: ',r)