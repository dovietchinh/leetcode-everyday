class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        size = len(nums)
        for i in range(size):
            j = i+1
            k = size - 1
            while j<k:
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] ==0:
                    res.add((nums[i],nums[j],nums[k]))
                    j += 1
                    k -= 1
                else:
                    break
        return list(res)