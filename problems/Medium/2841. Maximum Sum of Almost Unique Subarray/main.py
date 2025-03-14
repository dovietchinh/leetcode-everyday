from typing import *
class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        size = len(nums)
        if size == 0:
            return 0 
        if size == 1:
            return nums[0]

        counter = {}
        left,right = 0,k-1
        sum = 0
        result = float('-inf')
        for i in range(k):
            sum += nums[i]
            counter[nums[i]] = counter.get(nums[i],0) + 1
        while right < size:
            if len(counter) >= m:
                result = max(result,sum)
            sum -= nums[left]
            counter[nums[left]] -= 1
            if counter[nums[left]] == 0:
                del counter[nums[left]]
            left += 1
            right += 1
            if right == size:
                break
            counter[nums[right]] = counter.get(nums[right],0) + 1
            sum += nums[right]             
        return max(result,0)
if __name__ == '__main__':
    nums = [1,2,2]
    m,k=2,2
    r = Solution().maxSum(nums,m,k)
    print(r)