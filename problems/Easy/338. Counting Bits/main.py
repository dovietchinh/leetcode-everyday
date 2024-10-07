from typing import *
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            c = 0
            temp = i
            while temp !=0 :
                c += temp % 2 
                temp = temp // 2
            res.append(c)
        return res

        