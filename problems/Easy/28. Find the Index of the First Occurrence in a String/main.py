from typing import *
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        size = len(haystack)
        j = 0
        max_j = len(needle) - 1
        i = 0
        while i < size:
            print(i,j, haystack[i] ,needle[j])
            if haystack[i] == needle[j]:
                j += 1
            else:
                if j > 0:
                    i -= j
                    j = 0
            if j > max_j:
                return i - j + 1
            i += 1
        return -1 
            
        


            

        
    
if __name__ == '__main__':
    s = Solution().strStr("mississippi","issip")
    print(s)