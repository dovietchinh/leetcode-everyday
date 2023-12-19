from bisect import bisect_left
import itertools
import collections
class Solution:
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        diff = float('inf')
        res = 0
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if abs(target - s) < diff:
                    diff = abs(target - s)
                    res = s
                if s < target:
                    left += 1
                else:
                    right -= 1
        return res
                    
        

if __name__ == '__main__':
    a = [1,2,2,2,2,2,]
    # a = [0,1,2,3,4,5,6,7] 
    r = Solution().threeSumClosest([0,3,97,102,200],300)
    print(r)
