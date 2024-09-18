from typing import *
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)

        def backtracking(nums,tail=()):
            if not hasattr(backtracking,'result'):
                backtracking.result = []
            if len(nums) == 0:
                backtracking.result.append(tail)
                return
            for i in range(len(nums)):
                backtracking(nums[:i] + nums[i+1:],(*tail,nums[i]))
        backtracking(nums)
        return list(set(backtracking.result))

if __name__ == '__main__':
    # r = Solution().fourSum([1,0,-1,0,-2,2],0)
    # print(r)
    a = [1,1,2]
    b = Solution().permuteUnique(a)
    print(b)