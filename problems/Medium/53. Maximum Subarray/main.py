from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0 
        max_sum = float('-inf')
        for i in nums:
            sum += i
            max_sum = max(max_sum,sum,i)
            if sum < 0:
                sum = 0
        return max_sum
           
    

if __name__ == '__main__':
    # a = [-2,1,-3,4,-1,2,1,-5,4]
    a = [1]
    # a = [5,4,-1,7,8]
    # a = [1,-2]
    # a = [1,2,-1,-2,2,1,-2,1,4,-5,4]
    # a = [1,2,3]
    # a = [3,-2,-3,-3,1,3,0]
    # a = [-1,6,7,-7,-2,-6,-1,3,4,2,6,-3,-8,-1,7]
    # a = [1]
    # a = [9,0,-2,-2,-3,-4,0,1,-4,5,-8,7,-3,7,-6,-4,-7,-8]
    a = [-1,10,-12,3,4,5,-1]
    r = Solution().maxSubArray(a)
    print('r: ',r)