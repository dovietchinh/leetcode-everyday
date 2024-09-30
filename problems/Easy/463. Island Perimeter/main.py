from typing import *
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count_1 = 0
        count_connect = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue = [(i,j)]

                    while queue:
                        x,y = queue.pop(0)
                        if grid[x][y] == 1:
                            count_1 += 1
                            grid[x][y] = 2
                            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                                new_x = x + dx
                                new_y = y + dy
                                if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n or grid[new_x][new_y] == 0:
                                    continue
                                else:
                                    count_connect += 1
                                    queue.append((new_x,new_y))
                                # elif grid[new_x][new_y] == 1:
                                    
                    print('count_1: ',count_1)
                    print('count_connect: ',count_connect)
                    return count_1 * 4 - count_connect



if __name__ == '__main__':
    grid = [[1,0]]
    r = Solution().islandPerimeter(grid) 
    print(r)
        