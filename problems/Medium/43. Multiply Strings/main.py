from typing import *
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def char2int(c):
            return ord(c) - ord('0')
        num1 = [char2int(c) for c in num1[::-1]]
        num2 = [char2int(c) for c in num2[::-1]]
        memory = 0
        res = [0] * (len(num1) + len(num2))
        for m in range(len(num1)):
            for n in range(len(num2)):
                mul = num1[m] * num2[n] + res[m + n] + memory
                print('num1[m] * num2[n] + res[m + n] + memory', num1[m], num2[n], res[m + n], memory)
                print('mul', mul)
                memory = mul // 10
                print('memory', memory)
                char = mul % 10
                print('char', char)
                res[m + n] = char
                print('res', res)
            if memory > 0:
                res[m + n + 1] = memory
                memory = 0
        r = "".join([str(c) for c in res[::-1]])
        r = r.lstrip('0')
        if r == "":
            return '0'
        return r
        



            


        
        # print(res)

if __name__ == '__main__':
    num1 = "0"
    num2 = "0"
    s = Solution()
    print(s.multiply(num1, num2))
    print(int(num1) * int(num2))




            

