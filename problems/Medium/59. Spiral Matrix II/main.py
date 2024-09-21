from typing import *
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        def next_direction(i,j,direction): 
            a = i + direction[0]
            b = j + direction[1]
            if direction == [0,1]:
                if j == n -1 or matrix[a][b]!=0:
                    return [1,0]
            elif direction == [1,0]:
                if i == n -1 or matrix[a][b]!=0:
                    return [0,-1]
            elif direction == [0,-1]:
                if j == 0 or matrix[a][b]!=0:
                    return [-1,0]
            elif direction == [-1,0]:
                if i == 0 or matrix[a][b]!=0:
                    return [0,1]
            return direction
        direction = [0,1]
        i,j=0,0
        count = 1
        matrix = [[0]*n for _ in range(n)] 
        while count < n*n+1:
            matrix[i][j] = count
            direction = next_direction(i,j,direction)
            count += 1
            i = i + direction[0]
            j = j + direction[1]
        return matrix

if __name__ == '__main__'
    r = Solution().generateMatrix(5)
    for i in r:
        print(i)