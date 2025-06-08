from typing import *
import heapq
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        size = len(weights)
        w = []
        if k==1:
            return 0
        for index in range(size-1):
            i = weights[index] + weights[index+1]
            w.append(i)
        # print('w: ',w)
        w.sort()
        
        min_ = sum(w[:k-1])
        max_ = sum(w[-(k-1):])
        # print('w: ',w)
        # print('min: ',min_)
        # print('max: ',max_)
        return max_ - min_
        
        # check the max heap



if __name__ == '__main__':
    weights =  [25,74,16,51,12,48,15,5]
    k = 1
    r = Solution().putMarbles(weights,k)
    # print('r: ',r)
            


