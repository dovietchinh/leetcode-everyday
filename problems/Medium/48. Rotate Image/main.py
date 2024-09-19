from typing import *
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = n - 1
        for i in range(n//2+1):
            for j in range(i,m-i):
                if(matrix[i][j] == 18):
                    print(i,j)
                matrix[i][j],matrix[j][m-i],matrix[m-i][m-j],matrix[m-j][i] = matrix[m-j][i],matrix[i][j],matrix[j][m-i],matrix[m-i][m-j]
        # i,j = 0,0
        # matrix[i][j],matrix[j][m-i],matrix[m-i][m-j],matrix[m-j][i] = matrix[m-j][i],matrix[i][j],matrix[j][m-i],matrix[m-i][m-j]
        

if __name__ == '__main__':
    matrix2 = [[1,2,3],[4,5,6],[7,8,9]]
    matrix2 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    # matrix2 = [[2,29,20,26,16,28],[12,27,9,25,13,21],[32,33,32,2,28,14],[13,14,32,27,22,26],[33,1,20,7,21,7],[4,24,1,6,32,34]]
    for j in matrix2:
        print(j)
    Solution().rotate(matrix2)
    print('----------------')
    for j in matrix2:
        print(j)