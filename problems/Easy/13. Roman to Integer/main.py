class Solution:
    def romanToInt(self, s: str) -> int:
        LABEL = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IX": 9,
            "IV": 4,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM":900
        }
        result = 0
        skip = None
        for i in range(len(s)):
            if(i==skip):
                continue
            if s[i:i+2] in LABEL:
                result += LABEL[s[i:i+2]]
                skip = i+1
            else:
                result += LABEL[s[i]]
            i += 1
        return result


        

if __name__ == '__main__':
    for i in ["MCMXCIV"]: #3 58 1994
        r = Solution().romanToInt(i)
        print(r)
        """
        M CM XC IV
        1000 + 900 + 90 + 4
        """
        