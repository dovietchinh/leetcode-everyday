from typing import *
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        size = len(nums)
        sum = 0
        L = 0 
        R = 0
        result = float('-inf')
        while L < size:
            sum += nums[R%size]
            print('R,L: ',R,L,sum,result)
            R += 1
            result = max(result,sum)
            if sum < 0:
                sum = 0
                L = R
            if R - L + 1 > size:
                sum -= nums[L%size]
                result = max(result,sum)
                L+= 1
                while nums[L%size] < 0:
                    sum -= nums[L%size]                    
                    result = max(result,sum)
                    L += 1
        return result
        # R = 0 
        # L = 0 
        # sum = 0
        # for L in range(0,-size,-1): 
        #     sum += nums[L]
        #     result = max(result,sum)
        #     if sum < 0:
        #         sum = 0
        #         R = L
        
        # return result


if __name__ == '__main__':
    nums = [5,-3,5]
    nums = [1,-2,3,-2]
    nums = [-3,-2,-3]
    nums = [-2,4,-5,4,-5,9,4]
    r = Solution().maxSubarraySumCircular(nums)
    print(r)
        
    