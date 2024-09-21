from typing import *
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def next_direction(i,j,direction,visited):
            # nonlocal visited
            next_node = (i+direction[0],j+direction[1])
            if direction == [0,1]:
                if j == m -1 or next_node in visited:
                    return [1,0]
            elif direction == [1,0]:
                if i == n -1 or next_node in visited:
                    return [0,-1]
            elif direction == [0,-1]:
                if j == 0 or next_node in visited:
                    return [-1,0]
            elif direction == [-1,0]:
                if i == 0 or next_node in visited:
                    return [0,1]
            return direction
        n = len(matrix)
        m = len(matrix[0])
        direction = [0,1]
        res = []
        i,j = 0,0
        visited = set()
        while len(res) < m*n:
            # print(visited)
            # print(i,j)
            res.append(matrix[i][j])
            visited.add((i,j))
            direction = next_direction(i,j,direction,visited)
            i += direction[0]
            j += direction[1]
        return res

        

        
        



if __name__ == '__main__':
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    r = Solution().spiralOrder(matrix)
    print(r)