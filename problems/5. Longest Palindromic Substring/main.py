class Solution(object):
    def longestPalindrome(self, s):
        size = len(s)
        if(size<=1):
            return s
        max_value = 1
        r = s[0]
        for index,c in enumerate(s):
            max_step_to_expand = min(index,size -1 -index)+1
            left = True
            right = True 
            both = True 
            for i in range(1,max_step_to_expand+1):
                if i<=index:
                    if s[index-i] == s[index+i-1] and left:
                        if max_value < 2*i:
                            max_value = 2*i
                            r = s[index-i:index+i]
                    else:
                        left = False
                else:
                    left = False
                if i<= size-index-1:
                    if s[index-i+1] == s[index+i] and right:
                        if max_value < 2*i:
                            max_value = 2*i
                            r = s[index-i+1:index+i+1]
                    else:
                        right = False
                else:
                    right = False
                if i<=min(index,size-1-index):
                    if s[index-i] == s[index+i] and both:
                        if max_value < 2*i+1:
                            max_value = 2*i+1
                            r = s[index-i:index+i+1]
                    else:
                        both = False
                else:
                    both = False
        return r



        


if __name__ == '__main__':
    print(Solution().longestPalindrome("aacaaaaaa"))
