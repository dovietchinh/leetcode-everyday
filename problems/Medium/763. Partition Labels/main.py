from typing import *
from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        size = len(s)
        data = defaultdict(list)
        for i in range(len(s)):
            data[s[i]].append(i)
        
        intervals = []
        for k,v in data.items():
            interval = [v[0],v[-1]]
            intervals.append(interval)
        intervals.sort()
        # print('data: ',data)
        # print('intervals: ',intervals)
        previous_end = 0
        split_indexs = []
        for start,end in intervals:
            if start > previous_end:
                split_indexs.append(start)
            previous_end = max(end,previous_end)
        if len(split_indexs) == 0 or split_indexs[-1] != size :
            split_indexs.append(size)
        results = [split_indexs[0]]
        # print('split_indexs: ',split_indexs)
        for i in range(1,len(split_indexs)):
            results.append(split_indexs[i] - split_indexs[i-1])
        return results

# TC: 0(nlogn)
# SC: 0(n)
        
        


            

if __name__ == '__main__':
    s = "aaaaa"
    r = Solution().partitionLabels(s)
    print('r: ',r)