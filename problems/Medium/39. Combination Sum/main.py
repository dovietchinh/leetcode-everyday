from typing import List
import math
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        max_rep_outer = []
        for j in candidates:
            max_rep_outer.append(math.ceil(target/j))
        # print("max_rep: ",max_rep_outer)
        result_outer = []
        def fn(nums,max_rep,target_inner,tail=[]):
            # print('nums: ',nums)
            # print('max_rep: ',max_rep)
            if len(nums)==1:
                
                if ((target_inner % nums[0]) ==0) and target_inner/nums[0] <= max_rep[0]:
                    rep = target_inner/nums[0]
                    rep = int(rep)
                    a = [nums[0]]*rep
                    result_outer.append([*tail,*a])
            else:
                for j in range(max_rep[0]+1):
                    new_target = target_inner - nums[0]*j
                    if new_target < 0:
                        return 
                    a = [nums[0]]*j
                    new_tail = [*tail,*a]
                    fn(nums[1:],max_rep[1:],new_target,new_tail)
        init_tail = []
        fn(candidates,max_rep_outer,target)
        return result_outer
        # print("result_outer: ",result_outer)


if __name__ == '__main__':
    r = Solution().combinationSum([2,3,5],8)
    # print(r)