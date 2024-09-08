from typing import *
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        max_value = nums[-1]
        count_unique = 0
        current_value = None
        for i in range(len(nums)):
            if nums[i] != current_value:
                current_value = nums[i]
                count_unique += 1
                nums[count_unique-1] = nums[i]
            if nums[i] == max_value:
                break
        print(nums)
        return count_unique

        


            

        
    
if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1,1,2]))