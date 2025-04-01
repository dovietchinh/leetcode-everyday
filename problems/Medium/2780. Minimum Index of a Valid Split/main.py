from typing import *
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        size = len(nums)
        count = {}
        dominant_count = 0
        dominant_value = None
        for index in range(size):
            value = nums[index]
            if value not in count:
                count[value] = []
            count[value].append(index)
            if len(count[value]) > dominant_count:
                dominant_count = len(count[value])
                dominant_value = value 
        # print('dominant_value: ',dominant_value)
        # print('dominant_count: ',dominant_count)

        cnt = 0
        for index in range(size-1):
            # sencond array got the lenght : size - 1 - index
            if nums[index] == dominant_value:
                cnt += 1
            if (cnt / (index + 1)) <= 0.5:
                continue 
            if index != size -1:
                if (dominant_count - cnt) / (size - 1 - index) <= 0.5:
                    continue 
            else:
                if nums[index] != dominant_value:
                    return -1
                else:
                    return index 
            

            # print(f'index:{index}  cnt:{cnt} index+1:{cnt/(index+1)}')
            return index 
        return -1 
            
            
if __name__ == '__main__':
    nums =[2,1,3,1,1,1,7,1,2,1]
    r = Solution().minimumIndex(nums)
    print('r: ',r)