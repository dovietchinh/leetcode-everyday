from typing import *
import sys
from collections import defaultdict
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        prefix_minus = [nums[0]]
        for i in range(1,len(nums)):
            prefix_minus.append(nums[i] - nums[i-1])
        count = 0
        for query in queries:


if __name__ == '__main__':
    nums = [1,3,1,4,1,3,2]
    queries = [0,3,5]
    r = Solution().solveQueries(nums,queries)
    print('r: ',r)

