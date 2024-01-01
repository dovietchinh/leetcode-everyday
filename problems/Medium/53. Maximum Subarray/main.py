from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left,right = len(nums)//2,len(nums)//2
        total = nums[left]
        max_sum = total
        l,r = left,right
        while (right-left) <= len(nums)-1:
            print("left,right: ",left,right)
            if max_sum < total:
                max_sum = total
                l,r = left,right
            if left!=0 and right!=len(nums)-1:
                if nums[right+1] < nums[left-1]:
                    total += nums[left-1]
                    left -= 1
                else:
                    total += nums[right+1]
                    right +=1
                
            elif right==len(nums)-1:
                total += nums[left-1]
                left -= 1
            elif left==0:
                total += nums[right+1]
                right +=1
            else:
                continue
            
                

        print(nums[l:r+1])    
        return max_sum




if __name__ == '__main__':
    a = [-2,1,-3,4,-1,2,1,-5,4]
    a = [1]
    a = [5,4,-1,7,8]
    a = [1,-2]
    # a = [1,2,-1,-2,2,1,-2,1,4,-5,4]
    # a = [1,2,3]
    r = Solution().maxSubArray(a)
    print('r: ',r)