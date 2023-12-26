# import itertools
# class Solution:
#     def combine(self, n: int, k: int) :
def backtracking(nums,k):
    print('nums,k :',nums,k)
    if len(nums) == k:
        return [nums]
    if len(nums) < k:
        return []
    results = []
    for i in range(len(nums)):
        results += backtracking(nums[:i] + nums[i+1:],k) 
    return results
                
r = backtracking([1,2,3,4,5,6],3)
print(r)
print(len(r))
import itertools
r = itertools.combinations([1,2,3,4,5,6],3)
b = list(r)
print(b)
print(len(b))
