import bisect
class Solution:
    def searchRange(self, nums, target: int):
        start,end = -1,-1
        left,right = 0,len(nums) -1 
        last = False
        while left <= right:
            mid = (left + right)  //2
            print('left,mid,right: ',left,mid,right)
            if mid==left:
                last = True
            if nums[mid] == target:
                print('line12')
                if mid == 0:
                    start = mid 
                    break
                if nums[mid-1] == target:
                    right = mid
                else:
                    start = mid
                    break
            if target > nums[mid]:
                left = mid 
            else:
                right = mid
            if last:
                left += 1
            

        left,right = 0,len(nums) -1 
        last = False
        while left <= right:
            mid = (left + right) //2
            if mid == left:
                last = True
            if nums[mid] == target:
                if mid==len(nums)-1:
                    end = mid
                    break
                if nums[mid+1] == target:
                    left = mid
                else:
                    end = mid
                    break
            if target < nums[mid]:
                right = mid
            else:
                left = mid
            if last:
                left += 1
        return start,end
                 




def check():
    s = [1,3]
    t = 2
    l,r = 0,1
    while l<r:
        m = (l+r)//2
        if t < s[m]:
            r = m
        else:
            if l==m:
                break
            l = m
            


if __name__ == '__main__':
    r = Solution().searchRange([5,7,7,8,8,10],10)
    print(r)