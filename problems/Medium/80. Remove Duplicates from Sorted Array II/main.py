from typing import *
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        if size <= 2:
            return size
        left = 2
        right = 3

        while right < size:
            if left == right:
                right += 1
                continue 
            if nums[left] > nums[left-2]:
                left += 1
                continue 
            if nums[right] > nums[left-2]:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1
                continue
            else:
                right += 1
        if nums[left] > nums[left-2]:
            return left + 1
        return left 
        

            



if __name__ == '__main__':
    nums = [1,2,2,3,4,5,6]
    nums = [1,1,1,2,2,3]
    print(Solution().removeDuplicates(nums)) # 5
    print('nums:', nums)

