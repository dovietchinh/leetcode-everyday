from typing import *
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nearest = 0 
        farthest = nums[0]
        while nearest <= farthest:
            for i in range(nearest, farthest + 1):
                farthest = max(farthest, i + nums[i])
                if farthest >= len(nums) - 1:
                    return True
                nearest += 1
        return False

if __name__ == '__main__':
    
    r = Solution().canJump([3,2,1,0,4])
    print(r)