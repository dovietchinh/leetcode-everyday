class Solution(object):
    def search(self, nums,target):
        left,right = 0,len(nums) - 1
        # if right==-1:
        #     return -1
        # if nums[0] <= nums[-1]:
        #     return -1
        if len(nums)==1 and nums[0] == target:
            return 0
        if len(nums)==0:
            return -1
        while left<=right:
            mid = (left + right) //2
            n_left = nums[left]
            n_right = nums[right]
            n_mid = nums[mid]
            print('mid: ',mid)
            print('left: ',left)
            print('right: ',right)
            print('-----')
            
            if n_mid == target:
                return mid
            if n_left == target:
                return left
            if n_right == target:
                return right
            if mid==left:
                break
            if n_left < n_right:
                if target < n_mid:
                    right = mid
                else:
                    left = mid
            else:
                if n_left < n_mid:
                    if target < n_left:
                        left = mid
                    else:
                        if target < n_mid:
                            right = mid
                        else:
                            left = mid
                else:
                    if target > n_right:
                        right = mid
                    else:
                        if target < n_mid:
                            right = mid
                        else:
                            left = mid
        return -1

if __name__ == '__main__':
    r = Solution().search([1,3],1)
    print(r)