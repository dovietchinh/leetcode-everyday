from typing import *
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = 0
        p2 = 0
        while p1 < m and p2 < n:
            # print(nums1,p1,p2)
            if nums1[p1] <= nums2[p2]:
                p1 += 1
            else:
                nums1.insert(nums2[p2],p1)
                # p1 += 1
                p2 += 1
        for i in range(n):
            nums[m+i] =  nums2[i]
            

if __name__ == '__main__':
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    r = Solution().merge(nums1,3,nums2,3)
    print(nums1)