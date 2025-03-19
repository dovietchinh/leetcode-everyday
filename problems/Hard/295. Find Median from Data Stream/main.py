from typing import *
from bisect import bisect_left
class MedianFinder:
    def __init__(self):
        self.array = []
    def addNum(self, num: int) -> None:
        index = bisect_left(self.array,num)
        self.array.insert(index,num)
        
    def findMedian(self) -> float:
        if len(self.array) == 0:
            return None
        
        if len(self.array) %2 == 0:
            i = len(self.array) //2 
            return (self.array[i] + self.array[i-1]) / 2
        else:
            i = len(self.array) //2  
            return self.array[i]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
if __name__ == '__main__':
    m = MedianFinder()
    m.addNum(4)
    m.addNum(7)
    m.addNum(2)
    m.addNum(9)
    m.addNum(11)
    m.addNum(0)
    print(m.array)