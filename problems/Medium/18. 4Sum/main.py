from bisect import bisect_left
class Solution:
    def fourSum(self, nums, target: int):
        nums.sort()
        size = len(nums)
        results = set()
        for x1 in range(size-3):
            for x2 in range(x1+1,size):
                left = x2 + 1
                right = size - 1
                while left<right:
                    sum = nums[x1] + nums[x2] + nums[left] + nums[right]
                    print("sum: ",sum)
                    print("nums[x1],nums[x2],nums[left],nums[right]",nums[x1],nums[x2],nums[left],nums[right])
                    print('-------------------------------')
                    if sum==target:
                        results.add((nums[x1],nums[x2],nums[left],nums[right]))
                        # break
                        left += 1
                        right -= 1
                    if sum < target:
                        left += 1
                    if sum > target:
                        right -= 1
             
        return results

if __name__ == '__main__':
    # r = Solution().fourSum([1,0,-1,0,-2,2],0)
    # print(r)
    a = [-3,-2,-1,0,0,1,2,3]
    a.sort()
    b = Solution().fourSum(a,0)
    print(b)