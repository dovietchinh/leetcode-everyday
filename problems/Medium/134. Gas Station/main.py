from typing import *
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        size = len(gas)
        accumulate = 0
        current_index = 0
        total_sum = 0 
        for i in range(size):
            total_sum += gas[i] - cost[i]
            if accumulate < 0 and gas[i] - cost[i] > 0:
                accumulate = gas[i] - cost[i]
                current_index = i
            else:
                accumulate += gas[i] - cost[i]
        if total_sum >= 0 :
            return current_index 
        else:
            return -1
            

            
                

                




if __name__ == '__main__':
    # gas = [2,3,4]
    # cost = [3,4,3]
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    for i in range(len(gas)):
        print(gas[i] - cost[i])
        
    r = Solution().canCompleteCircuit(gas,cost)
    print('r: ',r)
    