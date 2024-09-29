class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) < 2:
            return False
        
        doubled_string = s + s
        substring_to_check = doubled_string[1:-1]
        return s in substring_to_check
     

if __name__ == '__main__':
    for i in ["MCMXCIV"]: #3 58 1994
        r = Solution().romanToInt(i)
        print(r)
        """
        M CM XC IV
        1000 + 900 + 90 + 4
        """
        