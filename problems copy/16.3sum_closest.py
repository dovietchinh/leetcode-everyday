from typing import *
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float('inf')
        min_value = float('inf')
        size = len(nums)
        print('nums: ',nums)
        for i in range(size-2):
            j = i+1
            k = size-1
            while j<k:
                print(nums[i], nums[j], nums[k])
                total = nums[i] + nums[j] + nums[k]
                if abs(total - target) < min_value:
                    res = total 
                    min_value = abs(total - target)
                if total < target:
                    j += 1
                elif total > target: 
                    k -= 1
                elif total == target:
                    return total  
                else:
                    continue 
        return res 

r = Solution().threeSumClosest([1,1,1,0],-100)
print(r)            



