class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        missing_value = n + 1
        for i in range(n):
            while 0 <= nums[i] <= n-1 and nums[nums[i]] != nums[i]:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return missing_value


if __name__ == '__main__':
    a = [1,2,0]
    a = [3,4,-1,1]
    # a = [7,8,9,11,12]
    a = [1,1000]
    # a = [1,2,5,3,6,8,4,3,6,8,5]
    a = [1,4,7,5,8,6,3,2]
    import random 
    a = list(range(20))
    random.shuffle(a)
    print('a: ',a)
    r = Solution().firstMissingPositive(a)
    print(r)