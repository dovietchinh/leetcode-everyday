from typing import *
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_value = 0
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                for k in range(j+1,len(points)):
                    area = self.calculate(points[i],points[j],points[k])
                    max_value = max(max_value,area)
        return max_value
    def calculate(self,a,b,c):
        x1,y1 = a 
        x2,y2 = b
        x3,y3 = c
        return 0.5 * abs(x1*y2 + x2*y3 + x3*y1 - x1*y3 - x2*y1 - x3*y2)
        


if __name__ == '__main__':
    pass