class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        size = len(s)
        start = False
        for i in range(size-1,-1,-1):
            if s[i]!=' ':
                if not start:
                    start = i
            else:
                if start:
                    return start - i 
        return start +1 


if __name__ == '__main__':
    r = Solution().plusOne([9,9,9,9])
    print(r)
        