from typing import *
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        # handle edge cases\
        if size==2:
            return [1,2]
        left = 0
        right = size - 1
        while left < right:
            sum = nums[left] + nums[right]
            if sum == target:
                return [left+1,right+1]
            elif sum < target:
                left += 1
            elif sum > target:
                right -= 1
        return 
        



        
        


if __name__ == '__main__':
    nums = [2,3,4]
    target = 6
    r = Solution().twoSum(nums,target)
    print('r: ',r)