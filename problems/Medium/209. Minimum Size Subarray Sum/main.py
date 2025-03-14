from typing import *
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        elif size == 1:
            return 1 if nums[0] >= target else 0
        left,right = 0,0
        sum = nums[0]
        result = float('inf')
        while right <=size:
            if sum >= target:
                result = min(result,right-left+1)
                sum -= nums[left]
                left += 1
            else:
                right += 1
                if right < size:
                    sum += nums[right]
        if result > size:
            return 0
        return result

            



if __name__ == '__main__':
    
    r = Solution().minSubArrayLen(4,[1,4,4])
    print("r: ",r)
    