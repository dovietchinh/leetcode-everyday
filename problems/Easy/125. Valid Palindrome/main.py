from typing import *
class Solution:
    def isPalindrome(self, s: str) -> bool:
        size = len(s)
        i = 0 
        j = size - 1
        while i < j:
            print('i,j:', i, j)
            if not s[i].lower().isalnum():
                i += 1
                continue
            if not s[j].lower().isalnum():
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False 
            i += 1
            j -= 1
        return True
        


if __name__ == '__main__':
    text = "A man, a plan, a canal: Panama"
    text = "race a car"
    text = " ;"
    r = Solution().isPalindrome(text)
    print(r)
        