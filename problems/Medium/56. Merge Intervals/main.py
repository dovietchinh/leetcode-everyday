from typing import *
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        current = intervals[0]
        for index in range(len(intervals)-1):
            if not current:
                current = intervals[index]
                continue
            if current[1] < intervals[index][0]:
                merged.append(current)
                current = intervals[index]
                continue
            else:
                if current[1] < intervals[index][1]:
                    current[1] = intervals[index][1]

        if current[1] < intervals[-1][0]:
            merged.append(current)
            merged.append(intervals[-1])
        else:
            if current[1] < intervals[-1][1]:
                current[1] = intervals[-1][1]
            merged.append(current)
        
        return merged






if __name__ == '__main__':
    r = Solution().merge([[1,3],[2,6],[8,10],[15,18]])
    print(r)