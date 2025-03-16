from typing import List
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix[0])
        m = len(matrix)
        self.prefix_sum = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    self.prefix_sum[i][j] = matrix[i][j]
                elif i == 0:
                    self.prefix_sum[i][j] = self.prefix_sum[i][j-1] + matrix[i][j]
                elif j == 0:
                    self.prefix_sum[i][j] = self.prefix_sum[i-1][j] + matrix[i][j]
                else:
                    self.prefix_sum[i][j] = self.prefix_sum[i][j-1] + self.prefix_sum[i-1][j] - self.prefix_sum[i-1][j-1] + matrix[i][j]    

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.prefix_sum[row2][col2]
        elif row1 == 0:
            return self.prefix_sum[row2][col2] - self.prefix_sum[row2][col1-1]
        elif col1 == 0:
            return self.prefix_sum[row2][col2] - self.prefix_sum[row1-1][col2]
        else:
            return self.prefix_sum[row2][col2] - self.prefix_sum[row1-1][col2] - self.prefix_sum[row2][col1-1] + self.prefix_sum[row1-1][col1-1]


if __name__ == '__main__':
    matrix = [[3, 0, 1, 4, 2],
              [5, 6, 3, 2, 1],
              [1, 2, 0, 1, 5],
              [4, 1, 0, 1, 7],
              [1, 0, 3, 0, 5]]
    obj = NumMatrix(matrix)
    for i in obj.prefix_sum:
        print(i)
    r = obj.sumRegion(2,1,4,3)
    print(r)
    r = obj.sumRegion(1,1,2,2)
    print(r)
    r = obj.sumRegion(1,2,2,4)
    print(r)
