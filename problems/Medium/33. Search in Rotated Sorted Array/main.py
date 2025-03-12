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
class Solution(object):
    def search(self, nums,target):
        left = 0
        right = len(nums) - 1
        if len(nums)==1:
            if nums[0] == target:
                return 0
            else:
                return -1
        while left < right:
            print('left: ,',left)
            print('right: ,',right)
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[left] < nums[right]: 
                if target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1

            elif nums[left] > nums[right]:
                # print('1')
                if nums[mid] <= nums[right]: #pivot on right-side of mid
                    if target > nums[mid] and target <= nums[right]:
                        left = mid + 1
                    else:
                        right = mid
                    # print('2')
                elif nums[mid] >= nums[left]: # pivot on left-side of mid
                    # print('3')
                    if target < nums[mid] and target >= nums[left]:
                        right = mid
                    else:
                        left = mid + 1

            elif nums[left] == nums[right]:
                if target < nums[mid]:
                    right = mid
                elif target > nums[mid]:
                    left = mid + 1

        return -1

if __name__ == '__main__':
    r = Solution().search([3,1],0)
    print(r)