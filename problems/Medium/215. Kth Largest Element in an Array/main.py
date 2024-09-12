import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        queue = []
        size = len(nums)
        for i in nums:
            heapq.heappush(queue,i*-1)
            # print('queue: ',queue)
        for i in range(k):
            r = heapq.heappop(queue)
        return -r

        

if __name__ == '__main__':
    pass