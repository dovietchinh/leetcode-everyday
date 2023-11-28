class Solution(object):
    def longestPalindrome(self, s):
        size = len(s)
        if(size<=1):
            return s
        max_value = 0
        r = ""
        
            
    def check_if_palindrome(self,s):
        size = len(s)
        for index in range(size>>2):

            if s[index] != s[size-1-index]:
                return False
        return True



if __name__ == '__main__':
    # for i in ["bb"]: 
    #     r = Solution().longestPalindrome(i)
    #     print(r)
    print(Solution().check_if_palindrome("asdsdsa"))