from typing import *
import heapq
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        l1 = len(nums1)
        l2 = len(nums2)
        queue1 = []
        queue2 = []
        
            
if __name__ == '__main__':
    # nums1 = [3,4,6,5]
    # nums2 = [9,1,2,5,8,3]
    # k = 5
    # nums1 = [6,7]
    # nums2 = [6,0,4]
    # k = 5
    nums1 = [5,9,3,7,5,6,2,3]
    nums2 = [3,8,1,2,8,6,0,8]
    k = 8
    r = Solution().maxNumber(nums1,nums2,k)
    print('r: ',r)