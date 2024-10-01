class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        size1 = len(num1)
        size2 = len(num2)
        i = size1 - 1
        j = size2 - 1
        res = []
        memory = 0
        while i >=0 or j >=0 or memory!=0:
            n1 = int(num1[i]) if i>=0 else 0
            n2 = int(num2[j]) if j>=0 else 0
            n = n1 + n2 + memory
            if n > 9:
                n = n - 10
                memory = 1
            else:
                memory = 0
            res.append(str(n))
            i -= 1
            j -= 1
        return ''.join(res[::-1])


if __name__ == '__main__':
    pass
        