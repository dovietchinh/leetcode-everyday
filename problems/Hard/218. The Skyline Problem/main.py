from typing import *
from collections import defaultdict
import heapq 
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        point_x = set()
        for building in buildings:
            point_x.add(building[0])
            point_x.add(building[1])
        point_x = sorted(list(point_x))
        point_y = [0] * len(point_x)
        for index,i in enumerate(point_x):
            for building in buildings:
                start,end,height = building
                if start <= i < end:
                    point_y[index] = max(point_y[index],height)
        res = []
        for index in range(len(point_x)):
            if len(res) == 0:
                res.append([point_x[index],point_y[index]])
            else:
                old_y = res[-1][1]
                x = point_x[index]
                y = point_y[index]
                if y != old_y:
                    res.append([x,y])
        return res
            

            
        
            

            
            
            
        

if __name__ == '__main__':
    buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    buildings = [[0,2,3],[2,5,3]]
    r = Solution().getSkyline(buildings)
    print(r)