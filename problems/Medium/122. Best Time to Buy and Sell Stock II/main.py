from typing import List 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        new_prices = []
        prev = None 
        for i in range(len(prices)):
            if prev is not None:
                if prices[i] == prev:
                    continue
            new_prices.append(prices[i])
            prev = prices[i]

        size = len(new_prices)
        if size == 1:
            return 0
        if size == 2:
            return max(0, new_prices[1] - new_prices[0])
        
        minimum_points,maximum_points = [],[]
        if new_prices[0] < new_prices[1]:
            minimum_points.append(0)
        else:
            maximum_points.append(0)

        for i in range(1, size-1):
            p_prev = new_prices[i-1]
            p = new_prices[i]
            p_next = new_prices[i+1]
            if p < p_prev and p < p_next:
                minimum_points.append(i)
            if p > p_prev and p > p_next:
                maximum_points.append(i)
        
        if new_prices[size-1] < new_prices[size-2]:
            minimum_points.append(size-1)
        else:
            maximum_points.append(size-1)
        
        i = 0
        j = 0 
        while i < len(minimum_points) and j < len(maximum_points):
            if minimum_points[i] < maximum_points[j]:
                profit += new_prices[maximum_points[j]] - new_prices[minimum_points[i]]
                i += 1
                j += 1
            else:
                j += 1
        return profit

if __name__ == '__main__':
    r = Solution().maxProfit([7,6,4,3,1])
    print('result', r)