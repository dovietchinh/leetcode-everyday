from typing import *
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        size = len(nums)
        left,right = 0, size - 1
        while left <= right: 
            mid = (left + right) // 2 
            print('left:', left, 'right:', right, 'mid:', mid)
            print('nums[left]:', nums[left], 'nums[right]:', nums[right], 'nums[mid]:', nums[mid])
            if target in [nums[mid], nums[left], nums[right]]:
                return True 
            if nums[left] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] < nums[right]:
                ## normal binary search
                if target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            elif nums[left] > nums[right]:
                #pivot in range
                if nums[left] > nums[mid]:
                    #pivot in left
                    if target < nums[mid] or target > nums[left]:
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    print('pivot in right')
                    if target < nums[right] or target > nums[mid]:
                        left = mid + 1
                    else:
                        right = mid - 1
                    
        return False


def generate_test():
    import random 
    arr = [random.randint(1, 1000) for _ in range(100)]
    arr.sort()
    k = random.randint(0, 100)
    arr = arr[k:] + arr[:k]
    target = random.randint(1, 1000)
    label = target in arr
    return arr,target,label


if __name__ == '__main__':
    # from tqdm import tqdm
    # for index in tqdm(range(100),total=100):
    #     arr,target,label = generate_test() 
    #     print(index)
    #     r = Solution().search(arr, target)
        
    #     if r!=label:
    #         print(arr, target, label, r)
    #         break

    nums = [1,1,1,1,1,1,0,1]
    target = 0.5
    r = Solution().search(nums, target)
    print(r)
    pass

    # arr = [659, 662, 682, 689, 701, 721, 725, 730, 732, 739, 744, 747, 748, 752, 757, 766, 774, 779, 781, 787, 802, 830, 830, 839, 864, 874, 874, 874, 880, 888, 915, 926, 927, 939, 952, 965, 970, 975, 981, 983, 996, 9, 51, 59, 70, 83, 88, 96, 103, 106, 107, 112, 124, 142, 147, 153, 165, 166, 177, 186, 202, 211, 217, 231, 231, 253, 259, 267, 284, 284, 301, 330, 333, 347, 353, 366, 367, 372, 392, 406, 429, 433, 433, 451, 502, 503, 506, 535, 542, 552, 566, 567, 586, 591, 592, 606, 621, 634, 643, 649] 
    # target = 965
    # r = Solution().search(arr, target)
    # print(r)
    # print(arr.index(target))
    # print(arr.index(max(arr)))
    