from typing import *
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        pass
        res = []
        def permute(n,tail=[]):
            size = len(n)
            if size == 0:
                res.append(tail)
            for i in range(size):
                permute(n[:i]+n[i+1:],[*tail,n[i]])
        permute(nums)
        return res
            



if __name__ == '__main__':
    r = Solution().permute([1,2,3,4])
    print(r)