from typing import *
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums)==1:
            if nums[0] == val:
                return 0
            else:
                return 1
        size = len(nums)
        slow_pointer = 0
        fast_pointer = 0
        while fast_pointer < size:
            print('slow_pointer, fast_pointer, nums:',slow_pointer,fast_pointer,nums)
            if slow_pointer == fast_pointer:
                fast_pointer += 1
                continue
            if nums[slow_pointer] == val:
                if nums[fast_pointer] == val:
                    fast_pointer += 1
                else:
                    nums[slow_pointer],nums[fast_pointer] = nums[fast_pointer],nums[slow_pointer]
                    slow_pointer += 1
                    fast_pointer += 1
            else:
                slow_pointer += 1
        while slow_pointer < size and nums[slow_pointer] != val:
            slow_pointer += 1
        return slow_pointer 
            
    
if __name__ == '__main__':
    s = Solution()
    print(s.removeElement([3,3],6))