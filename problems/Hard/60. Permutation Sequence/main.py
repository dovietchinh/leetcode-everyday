class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        list_ = [str(i) for i in range(1,n+1)]
        count = 0
        results = None
        def permutation(nums,tail=[]):
            nonlocal results,count
            if len(nums) == 0:
                count += 1
                if count == k:
                    results = tail
                    return True
                else:
                    return False
            else:
                for i in range(len(nums)):
                    temp = permutation(nums[:i]+nums[i+1:],[*tail,nums[i]])
                    if temp:
                        return temp
                    
        a = permutation(list_)
        return ''.join(results)
        
                


if __name__ == '__main__':
    r = Solution().getPermutation(3,1)
    print('r: ',r)