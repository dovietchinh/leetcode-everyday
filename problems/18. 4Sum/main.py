from bisect import bisect_left
class Solution:
    def fourSum(self, nums, target: int):
        nums.sort()
        size = len(nums)
        results = set()
        for i in range(size-3):
            if nums[i] + 3*nums[-1] < target:
                break
            if nums[i]*4 > target:
                break
            for j in range(i+1,size-2):
                if nums[i] + nums[j] + 2*nums[-1] < target:
                    break
                if nums[i] + nums[j]*3 > target:
                    break
                for k in range(j+1,size-1):
                    if nums[i] + nums[j] + nums[j] + nums[-1] < target:
                        break
                    if nums[i] + nums[j] + 2*nums[j] > target:
                        break
                    search_value = target -  (nums[i] + nums[j] + nums[k])
                    search_index = bisect_left(nums[k:],search_value)
                    if(nums[search_index + k] == search_value):
                        results.add((nums[i],nums[j],nums[k],nums[search_index+k]))
                    
        return list(results)


def n_sum(nums,n,target):
    print('nums,n,target',nums,n,target)
    if n==1:
        index = bisect_left(nums,target)
        if nums[index] == target:
            return [[target]]
        else:
            return None
    results = set()
    for i in nums[:-(n-1)]:
        # if nums[i]*n > target:
        #     break
        # if nums[i] + (n-1) * nums[-1] < target:
        #     break
        before = n_sum(nums[i:],n-1,target-i)
        if before is None:
            continue
        for j in before:
            try:
                results.add((nums[i],*j))
            except:
                print('error')
                print(nums[i],j)
    return list(results)


if __name__ == '__main__':
    # r = Solution().fourSum([1,0,-1,0,-2,2],0)
    # print(r)
    a = [1,0,-1,0,-2,2]
    a.sort()
    b = n_sum(a,4,0)
    print(b)