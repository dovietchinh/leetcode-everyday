from typing import *
class Solution:
    def jump(self, nums: List[int]) -> int:

        # greedy

        minimal_step = len(nums) + 1 
        if len(nums) == 1:
            return 0
        def jum_to_n(n,current_step=0):
            nonlocal minimal_step
            if current_step >= minimal_step:
                return False
            if n[0] == 0:
                return 
            if len(n)<=1:
                if current_step < minimal_step:
                    minimal_step = current_step
                return
            max_step_can_jump = n[0]
            max_value = -1
            max_index = -1
            # print(n)
            max_can_jum = min(n[0],len(n)-1)
            if n[0] >= len(n) - 1:
                if current_step+1 < minimal_step:
                    minimal_step = current_step+1
                return
            # print("max_can_jum: ",max_can_jum)
            for index in range(max_can_jum,0,-1):
                # print('index: ',index)
                if max_value < n[index]:
                    max_value = n[index]
                    max_index = index 
            jum_to_n(n[max_index:],current_step+1)
        jum_to_n(nums)
        return minimal_step
                


                


        




if __name__ == '__main__':
    n = [2,3,1,1,4]
    n = [3,2,1]
    # n = [8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]
    r = Solution().jump(n)
    print(r)