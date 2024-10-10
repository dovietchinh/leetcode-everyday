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
        
        peak_down,peak_up = [],[]
        if new_prices[0] < new_prices[1]:
            peak_down.append(0)
        else:
            peak_up.append(0)

        for i in range(1, size-1):
            p_prev = new_prices[i-1]
            p = new_prices[i]
            p_next = new_prices[i+1]
            if p < p_prev and p < p_next:
                peak_down.append(i)
            if p > p_prev and p > p_next:
                peak_up.append(i)
        
        if new_prices[size-1] < new_prices[size-2]:
            peak_down.append(size-1)
        else:
            peak_up.append(size-1)
        
        i = 0
        j = 0 
        while i < len(peak_down) and j < len(peak_up):
            if peak_down[i] < peak_up[j]:
                profit += new_prices[peak_up[j]] - new_prices[peak_down[i]]
                i += 1
                j += 1
            else:
                j += 1
        return profit

if __name__ == '__main__':
    r = Solution().maxProfit([7,6,4,3,1])
    print('result', r)