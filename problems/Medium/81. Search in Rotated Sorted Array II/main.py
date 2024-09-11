from typing import *
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        size = len(nums)
        left,right = 0, size - 1
        while left <= right: 
            mid = (left + right) // 2 
            # print('left:', left, 'right:', right, 'mid:', mid)
            if target in [nums[mid], nums[left], nums[right]]:
                return True 
            if nums[left] > nums[mid]: 
                # pivot point in range(left-mid)
                if nums[left] < target:
                    right = mid - 1
                elif target < nums[mid]:
                    right = mid - 1
                elif target < nums[right]:
                    right = mid - 1
                else:
                    left += 1
                    right -= 1
            elif nums[mid] == nums[left]:
                if nums[mid] < nums[right]:
                    left = mid + 1
                elif nums[mid] > nums[right]:
                    right = mid - 1
                else: 
                    left += 1
                    right -= 1
            else: 
                # pivot point in range(mid-right)
                if nums[left] < target:
                    right = mid - 1
                elif target > nums[mid]:
                    left = mid + 1
                elif target < nums[right]:
                    left = mid + 1
                else:
                    left += 1
                    right -= 1
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
    from tqdm import tqdm
    for index in tqdm(range(100),total=100):
        arr,target,label = generate_test() 
        print(index)
        r = Solution().search(arr, target)
        
        if r!=label:
            print(arr, target, label, r)
            break
    # r = Solution().search(nums, target)
    # print(r)

    [559, 583, 604, 607, 610, 611, 612, 615, 622, 645, 651, 664, 672, 673, 692, 699, 701, 704, 727, 729, 729, 765, 766, 774, 787, 792, 795, 798, 803, 827, 838, 840, 845, 855, 856, 863, 907, 908, 913, 915, 920, 922, 930, 933, 940, 941, 945, 983, 997, 2, 5, 14, 28, 39, 39, 48, 63, 67, 73, 76, 85, 128, 128, 137, 145, 158, 161, 170, 179, 184, 187, 188, 198, 204, 256, 260, 295, 336, 339, 352, 357, 382, 392, 402, 413, 415, 418, 423, 434, 441, 450, 451, 455, 458, 464, 478, 482, 500, 509, 539] 
    699