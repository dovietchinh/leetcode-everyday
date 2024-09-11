from typing import * 
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])
        left,right = 0, len(matrix) * len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) // 2 
            index_row = mid // n 
            index_col = mid % n
            if matrix[index_row][index_col] == target:
                return True
            elif matrix[index_row][index_col] < target:   
                left = mid + 1
            elif matrix[index_row][index_col] > target:   
                right = mid - 1
            else:
                return False
        return False 


if __name__ == '__main__':
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    r = Solution().searchMatrix(matrix, target)