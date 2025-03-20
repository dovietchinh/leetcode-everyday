from typing import *
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = {}
        size = len(nums)
        if size == 1:
            return nums
        # if size <= 2:
        #     return nums
        # save 3 value_which_most_occurs 
        temp = {}
        for i in nums:
            # if len(counter) < 3:
            if i not in counter:
                counter[i] = 0
            counter[i] += 1
            if len(temp) <= 3:
                temp[i] = counter[i]
            else:
                sorted_keys = sorted(list(temp.keys()),key=lambda x:temp[x])
                if counter[i] > temp[sorted_keys[0]]:
                    del temp[sorted_keys[0]]
                    temp[i] = counter[i]
        results = []
        for k,v in temp.items():
            if v > size // 3:
                results.append(k)
        print('temp: ',temp)
        print('size: ',size)
        return results
if __name__ == '__main__':
    nums = [2,2]
    r = Solution().majorityElement(nums)
    print(r)






                




            
