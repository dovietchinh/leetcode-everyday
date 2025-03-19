from typing import *
# from collections import OrderedDcit
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        size = len(s)
        # handle edge case 
        if size < len(p):
            return []

        counter_p = dict()
        for i in p:
            if i not in counter_p:
                counter_p[i] = 0
            counter_p[i] += 1
        data = dict()
        left = 0
        for right in range(len(p)):
            if s[right] not in data:
                data[s[right]] = 0
            data[s[right]] += 1
        results = []
        # if counter_p == data:
        #     resutls.append(0)
        while right < size:
            if data == counter_p:
                results.append(left)
            
            right += 1
            if right == size:
                break 
            if s[right] not in data:
                data[s[right]] = 0
            data[s[right]] += 1
            data[s[left]] -= 1
            if data[s[left]] == 0:
                del data[s[left]]
            left += 1

        return results
        
    

            
        

if __name__ == '__main__':
    s = "abab"
    p = "ab"
    r = Solution().findAnagrams(s,p)
    print(r)