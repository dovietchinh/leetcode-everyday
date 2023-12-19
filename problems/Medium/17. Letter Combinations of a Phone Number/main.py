
class Solution:
    def letterCombinations(self, digits: str):
        TEXT = [None,None,"abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        size = len(digits)
        max_value = 1
        base_digits = []
        if len(digits)==0:
            return []
        for index,digit in enumerate(digits[::-1]):
            base_digits.insert(0,max_value)
            temp = max_value * len(TEXT[digit])
            max_value = temp 
        results = []
        for n in range(max_value):
            c = ''
            for index in range(0,size):
                value = n // base_digits[index]
                c += TEXT[digits[index]][value]
                n -= value * base_digits[index]
            results.append(c)
        return results
            
if __name__ == '__main__':
    r = Solution().letterCombinations([2,3])
    print(r)