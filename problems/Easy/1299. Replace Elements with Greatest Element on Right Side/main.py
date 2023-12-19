from typing import List
import random
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        if len(arr) == 1:
            return [-1]
        new_arr = []
        new_arr.append(-1)
        max_value = arr[-1]
        for index in range(len(arr)-1,0,-1):
            new_arr.insert(0,max_value)
            if max_value < arr[index-1]:
                max_value = arr[index-1]
        return new_arr

if __name__ == '__main__':
    arr = random.sample(range(100),10)
    a = Solution().replaceElements(arr)
    print(arr)
    print(a)

        


