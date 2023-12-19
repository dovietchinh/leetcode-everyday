class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start = 0
        max_value = 1
        if len(s)<2:
            return len(s)
        for end in range(1,len(s)):
            c = s[end]
            try:
                if max_value < end - start:
                    max_value = end - start
                index = s.index(c,start,end)
                start = index + 1
            except:
                index = None
                if max_value < end + 1 - start:
                    max_value = end - start + 1
        
        return max_value
    
            
            



if __name__ == '__main__':
    for i in ["aab","abba","pwwkew","abcabcbb"]: 
        r = Solution().lengthOfLongestSubstring(i)
        print(r)
    