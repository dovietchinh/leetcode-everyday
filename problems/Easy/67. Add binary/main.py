from typing import *
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        i = len(a) - 1
        j = len(b) - 1
        memo = 0
        while i >= 0 or j >= 0 or memo !=0:
            v1 = a[i] if i >= 0 else 0 
            v2 = b[j] if j >= 0 else 0
            r = int(v1) + int(v2) + memo
            memo = r // 2
            r = r%2
            res.append(str(r))
            i -= 1
            j -= 1
        return ''.join(res[::-1])

if __name__ == '__main__':
    a,b = "1010", "1011"
    r = Solution().addBinary(a,b)
    print(r)
        