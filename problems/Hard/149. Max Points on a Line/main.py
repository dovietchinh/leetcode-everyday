class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        size = len(points)
        if size in [1,2]:
            return size
        for i in range(size):
            for j in range(i+1,size):
                p1 = points[i]
                p2 = points[j]
                x1,y1 = p1
                x2,y2 = p2

if __name__ == '__main__':
    pass