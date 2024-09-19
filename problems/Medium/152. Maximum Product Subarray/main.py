from typing import *
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        start = 0
        end = 0
        max_product = float('-inf')
        product = 1
        while end < len(nums):
            
            product = product * nums[end]
            # print('start,end,product: ', start,end,product)
            max_product = max(max_product,product)
            if product < 0:
                product  /= nums[start]
                start += 1
                max_product = max(product,max_product)
                # print('start,end,product2: ', start,end,product)
            elif product == 0:
                start += 1
                product = 1
                for j in range(start,end+1):
                    product *= nums[j]
                max_product = max(product,max_product)
                # print('start,end,product3: ', start,end,product)
            end += 1
        # print('start,end: ', start,end)
        # print('nums[start:end+1]: ', nums[start:end+1])
        # print('solution_point: ', solution_point)   
        return int(max_product)
        



if __name__ == '__main__':
    import random 
    a = [random.randint(-10,10) for i in range(20)]
    max_value = float('-inf')
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            m = 1 
            for k in range(i,j):
                m *= a[k]
            print('i,j: m ', i,j,m)
            max_value = max(m,max_value)
    print('max_value: ', max_value)
    r = Solution().maxProduct(a)
    print(r)