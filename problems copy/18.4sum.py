from typing import *
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        size = len(nums)
        if size < 4:
            return []
        res = set()
        print(nums)
        for a in range(size-3):
            for b in range(a+1,size-2):
                c = b + 1
                d = size - 1
                while c < d :
                    print((nums[a],nums[b],nums[c],nums[d]))
                    total = nums[a] + nums[b] + nums[c] + nums[d]
                    if total < target:
                        c += 1
                    elif total > target:
                        d -= 1
                    elif total == target:
                        # if nums[c]!=nums[d]:
                        res.add((nums[a],nums[b],nums[c],nums[d]))
                        c += 1
                        d -= 1
                    else:
                        break 
        return list(res)

r = Solution().fourSum([1,0,-1,0,-2,2],0)
print(r)
                    


        