from typing import *
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums2 = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue 
            nums2.append(nums[i])
        size = len(nums2)
        if size <= 1:
            return sum(nums2)
        if size == 2:
            return max(nums2)
        sum2 = 0         
        # a = []
        if nums[0] > nums2[1]:
            sum2 += nums2[0]
        
        # print('nums2: ', nums2)
        for i in range(1,size-1):
            # print(nums2[i],a)
            # if nums[i-1] == nums[i]:
            #     continue
            if nums2[i] >= nums2[i+1] and nums2[i] >= nums2[i-1]:
                sum2 += nums2[i]
                # a.append(nums2[i])
            if nums2[i] <= nums2[i+1] and nums2[i] <= nums2[i-1]:
                sum2 -= nums2[i]
                # a.append(nums2[i])
        if nums2[-1] > nums2[-2]:
            sum2 += nums2[-1]
            # a.append(nums2[-1])
        # print('a: ', a)
        return sum2

        
        


if __name__ == '__main__':
    # nums = [4,2,5,3]
    # nums = [7,1,1,2,4] #10
    nums = [4,3,13,4,12,12,20,9,2,15] #43
    # nums = [2,1,5,4,4] #6 
    r = Solution().maxAlternatingSum(nums)
    print(r)
    