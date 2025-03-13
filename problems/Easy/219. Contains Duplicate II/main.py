from typing import *
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        size = len(nums)
        if size<=1:
            return False
        if k ==0:
            return False
        if size==2 and k!=0:
            return nums[0]==nums[1]
        left,right = 0,0
        storage = set()
        # storage.add(nums[left])
        for right in range(size):
            if right - left <= k:
                if nums[right] in storage:
                    # print('left,right: ',left,right)
                    return True
                storage.add(nums[right])
            else:
                storage.remove(nums[left])
                left +=1
                if nums[right] in storage:
                    # print('left,right: ',left,right)
                    return True
                storage.add(nums[right])
        return False
            
