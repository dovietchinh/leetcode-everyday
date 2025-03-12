from typing import List
# import collections
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        seen = {}
        for i in candidates:
            if i not in seen:
                seen[i] = 0
            seen[i] += 1
        counter_outer = list(seen.items())
        def permutation(counter,new_target,tail=[]):
            if len(counter)==0 or new_target < 0:
                return 
            k,v = counter[0]

            for i in range(v+1):
                temp = [k] * i 
                if (k*i) == new_target:
                    results.append([*tail,*temp])
                else:
                    # new_counter = counter.copy()
                    # new_counter.pop(k)
                    # new_target = new_target - k*i
                    permutation(counter[1:],new_target - k*i,[*tail,*temp])
        permutation(counter_outer,target)
        return results
        
if __name__ == '__main__':
    a = [14,6,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12]
    target = 27
    r = Solution().combinationSum2(a,27)
    print(r)
    # print('------------')
    # for i in r:
    #     print(i)