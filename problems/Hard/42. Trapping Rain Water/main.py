from typing import *
class Solution:
    def trap(self, nums: List[int]) -> int:
        # convert height to list 
        size = len(nums)
        ## handle edge case
        if size < 3:
            return 0
        
        temp = list(enumerate(nums))  ## index-value pair
        sorted_height = sorted(temp,key= lambda x:-x[1])   # sorted height based on value
        # print('sorted_height:',sorted_height)
        index1,height1 = sorted_height[0]
        index2,height2 = sorted_height[1]
        min_index = min(index1,index2)
        max_index = max(index1,index2)
        area = 0
        # data = {}
        for i in range(min_index,max_index):
            area += max(height2 - nums[i],0)
            # data[i] = max(height2 - nums[i],0)
        for i in range(2,size):
            index,height = sorted_height[i]
            if min_index < index < max_index:
                continue 
            elif index < min_index:
                for j in range(index+1,min_index):
                    area += max(height - nums[j],0)
                    # data[j] = max(height2 - nums[i],0)
                min_index = index
            elif index > max_index:
                for j in range(max_index,index):
                    area += max(height - nums[j],0)
                    # data[j] = max(height2 - nums[i],0)
                max_index = index
        # print('data:',data)
        return area            
                
    

if __name__ == '__main__':
    nums = [0,1,0,2,1,0,1,3,2,1,2,1]
    nums = [4,2,0,3,2,5]
    nums = [0]
    r = Solution().trap(nums)
    print(r)
    

