from typing import *
import math
def asd(l,r):
    l1 = math.floor(math.log(l,4))
    l2 = math.floor(math.log(r,4))

    a = l - 4**l1
    b = r - 4**l2 + 1
    total = 0
    print('l1: ,l2: ',l1,l2)
    print('a,b: ',a,b)
    for i in range(l1,l2):
        total += 3*(i+1)*4**i
    total = total - a*(l1+1) + (l2+1) * b 
    if total % 2 == 0:
        return int(total / 2)
    else:
        return int(total //2 + 1)
class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        count = 0
        for l,r in queries:
            count += asd(l,r)
        return count



r = asd(1,2)


print(r)