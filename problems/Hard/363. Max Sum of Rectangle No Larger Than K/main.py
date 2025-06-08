from typing import *
def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        pass

from sortedcontainers import SortedList
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = -math.inf
        for r1 in range(m):
            arr = [0] * n  # arr[i] is sum(matrix[r1][c]...matrix[r2][c])
            for r2 in range(r1, m):
                for c in range(n): arr[c] += matrix[r2][c]
                ans = max(ans, self.maxSumSubAarray(arr, n, k))
        return ans

    def maxSumSubAarray(self, arr, n, k):
        right = 0  # PrefixSum so far
        seen = SortedList([0])
        ans = -math.inf
        for i in range(n):
            right += arr[i]
            left = self.ceiling(seen, right - k)  # right - left <= k -> left >= right - k
            if left != None:
                ans = max(ans, right - left)
            seen.add(right)
        return ans

    def ceiling(self, sortedList, key):  # O(logN)
        idx = sortedList.bisect_left(key)
        if idx < len(sortedList): return sortedList[idx]
        return None
                    
if __name__ == '__main__':
    matrix = [[1,0,1],[0,-2,3]]
    k = 2
    matrix = [[5,-4,-3,4],[-3,-4,4,5],[5,1,5,-4]]
    print_matrix(matrix)
    k = 3
    r = Solution().maxSumSubmatrix(matrix,k)
    print(r)


