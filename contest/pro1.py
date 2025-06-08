from typing import *
class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        results = []
        min_value = float('inf')
        for i in cost:
            min_value = min(min_value,i)
            results.append(min_value)
        return results
            
if __name__ == '__main__':
    cost = [1,2,4,6,7]
    r = Solution().minCosts(cost)
    print('r: ',r)