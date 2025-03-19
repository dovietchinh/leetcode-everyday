from typing import *
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        size = len(nums)
        # handle edge case
        if size == 3:
            if sum(nums) == 0:
                return 1
            elif sum(nums) == 3:
                return 0
            else:
                return -1 
        count = 0 
        for i in range(size-3):
            if nums[i] != 1:
                count += 1
                nums[i] = 1 - nums[i]
                nums[i+1] = 1 - nums[i+1]
                nums[i+2] = 1 - nums[i+2]
        if sum(nums[-3:]) == 0:
            return count + 1
        elif sum(nums[-3:]) == 3:
            return count 
        else:
            return -1



    



if __name__ == '__main__':
    nums = [0,1,1,1]
    r = Solution().minOperations(nums)
    print(r)
    
