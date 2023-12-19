from bisect import bisect_left

class Solution:
    def threeSum(self, nums):
        nums.sort() #nlogn
        size = len(nums)
        results = set()
        old_i = None
        old_j = None
        for i in range(size-2):
            old_j = None
            num_i = nums[i]
            if num_i == old_i:
                continue
            old_i = nums[i]
            for j in range(i+1,size-1):
                print('i,j: ',i,j)
                if nums[j] == old_j:
                    continue
                seach_value = 0 - (nums[i] + nums[j])
                if seach_value > nums[-1] or seach_value < nums[j+1]:
                    continue
                k = bisect_left(nums[j+1:],seach_value)
                if nums[j+1+k]==seach_value:
                    results.add((nums[i],nums[j],nums[j+1+k]))
                old_j = nums[j]
                
            
        return results
        
if __name__ == '__main__':
    a = [1,2,3,5,7,8,9,10]
    # a = [0,1,2,3,4,5,6,7] 
    r = Solution().threeSum([3,0,-2,-1,1,2])
    print(r)
