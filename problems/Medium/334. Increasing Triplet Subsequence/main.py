from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i = 0
        size = len(nums)
        j = 0
        k = 0
        for index in range(size):
            if nums[index] > nums[j] and j!=0:
                k = index
                # print(i,j,k)
                return True
            if j==0:
                if nums[index] > nums[i]:
                    j = index
            else:
                if nums[j] > nums[index] > nums[i]:
                    j = index
            if nums[index] < nums[i]:
                i = index
        return False  
        
if __name__ == '__main__':
    nums = [2,1,5,0,4,6]
    r = Solution().increasingTriplet(nums)
    print('r: ',r)
    