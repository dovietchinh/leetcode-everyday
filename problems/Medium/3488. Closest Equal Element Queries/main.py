from typing import *
import sys
from collections import defaultdict
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        size = len(nums)
        mymap = defaultdict(list)
        for i in range(size):
            value = nums[i]
            mymap[value].append(i)
        min_distance = {}
        print('mymap: ',mymap)
        for v,l_index in mymap.items():
            
            len_ = len(l_index)
            if len_==1:
                min_distance[v] = -1 
                continue
            min_value = sys.maxsize
            for index in range(len_):
                if index == 0:
                    temp = size - (l_index[-1] - l_index[0])
                else:
                    temp = (l_index[index] - l_index[index-1])
                min_value = min(min_value,temp)
            min_distance[v] = min_value 
        results = []
        for query in queries:
            value = nums[query]
            results.append(min_distance[value])
        return results


if __name__ == '__main__':
    nums = [1,3,1,4,1,3,2]
    queries = [0,3,5]
    r = Solution().solveQueries(nums,queries)
    print('r: ',r)

