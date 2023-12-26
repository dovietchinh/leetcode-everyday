import random 
nums = list(range(40)) + list(range(40))
random.shuffle(nums)
def sort_first_n(nums,n):
    n = len(nums)
    for i in range(len(nums)):  
        print('i: ',i)  
        while 0 <= nums[i] <= n-1 and nums[nums[i]] != nums[i]:
            print(f'swap: nums[i]={nums[i]} and nums[nums[i]]={nums[nums[i]]}')
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        print('nums: ',nums)


sort_first_n(nums,0)