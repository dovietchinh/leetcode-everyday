from typing import *
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        size = len(nums)
        heap = [[nums[0],0],[nums[1],1]]
        heapq.heapify(heap)
        if k!= 2:
            for i in range(2,k):
                if nums[i] > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap,(nums[i],i))  # heap[0] is always the second largest in the heap
        #so heap[0] is second largest
        # heap[1] is the largest  
        res = [heap[1][0]]
        for index in range(k,size):
            last = nums[index]
            if index - k == heap[0][1]:
                heap = [heap[1]]
            elif index - k == heap[1][1]:
                heap = [heap[0]]

            print('heap: ',heap)

            if last > heap[0][0]:    
                if len(heap) == 2:
                    heapq.heappop(heap)
                heapq.heappush(heap,[last,index])
            else:
            res.append(heap[1][0])
        print(res)            



if __name__ == '__main__':
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    r = Solution().maxSlidingWindow(nums,k)
    print(r)


