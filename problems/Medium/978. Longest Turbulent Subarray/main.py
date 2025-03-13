from typing import *
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        size = len(arr)
        if size <= 1:
            return size
        if size == 2:
            return 1 if arr[0] == arr[1] else 2
        count_max_lenght = 1   
        left = 0
        right = 0 
        while right < size - 1:
            if left == right:
                if arr[left] == arr[left + 1]:
                    left += 1
                right += 1
            else:
                if arr[right - 1] < arr[right] and arr[right] > arr[right + 1]:
                    right += 1
                elif arr[right - 1] > arr[right] and arr[right] < arr[right + 1]:
                    right += 1
                else:
                    left = right
            count_max_lenght = max(count_max_lenght, right - left + 1)
        return count_max_lenght



            



if __name__ == '__main__':
    arr = [9,4,2,10,7,8,8,1,9]
    r = Solution().maxTurbulenceSize(arr)
    print(r)
    
