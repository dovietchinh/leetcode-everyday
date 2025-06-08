from typing import *
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
    
        cache = {}
        def longestPalindromeArray(a,b,c,d):
            nonlocal cache
            if (a,b,c,d) in cache:
                return cache.get((a,b,c,d))
            if a==-1 and b==-1:
                if c > d:
                    cache[(a,b,c,d)] = True 
                    return True 
                if c==d:
                    cache[(a,b,c,d)] = True 
                    return True 
                if t[c] == t[d] and longestPalindromeArray(-1,-1,c+1,d-1):
                    del cache[(-1,-1,c+1,d-1)]
                    cache[(a,b,c,d)] = True
                    return True
                cache[(a,b,c,d)] = False
                return False 
            if c==-1 and d==-1:
                if a>b:
                    cache[(a,b,c,d)] = True 
                    return True 
                if a==b:
                    cache[(a,b,c,d)] = True
                    return True 
                if s[a] == s[b] and longestPalindromeArray(a+1,b-1,-1,-1):
                    del cache[(a+1,b-1,-1,-1)]
                    cache[(a,b,c,d)] = True
                    return True
                cache[(a,b,c,d)] = False
                return False 

            if a==b and c==d:
                cache[(a,b,c,d)] = s[a] == t[c]
                return s[a] == t[c]
            if a==b:
                if s[a] ==t[d] and longestPalindromeArray(-1,-1,c,d-1):
                    del cache[(-1,-1,c,d-1)]
                    cache[(a,b,c,d)] = True
                    return True
                cache[(a,b,c,d)] = False
                return False 
            if c==d:
                if s[a] ==t[d] and longestPalindromeArray(a+1,b,-1,-1):
                    del cache[(a+1,b,-1,-1)]
                    cache[(a,b,c,d)] = True
                    return True
                cache[(a,b,c,d)] = False
                return False 
            if s[a] == t[d] and longestPalindromeArray(a+1,b,c,d-1):
                del cache[(a+1,b,c,d-1)]
                cache[(a,b,c,d)] = True
                return True
            cache[(a,b,c,d)] = False
            return False 
                
        max_size = -1
        for a in range(len(s)):
            for b in range(a,len(s)):
                for c in range(len(t)):
                    for d in range(c,len(t)):
                        if longestPalindromeArray(a,b,c,d):
                            l = b-a +1 + d-c + 1
                            max_size = max(max_size,l)
                            if max_size == 5:
                                print(a,b,c,d)
        for a in range(len(s)):
            for b in range(a,len(s)):
                if longestPalindromeArray(a,b,-1,-1):
                    l = b-a +1 
                    max_size = max(max_size,l)
                    if max_size == 5:
                        print(a,b,c,d)


        for c in range(len(t)):
            for d in range(c,len(t)):
                if longestPalindromeArray(-1,-1,c,d):
                    l = d - c + 1
                    max_size = max(max_size,l)
                    if max_size == 5:
                        print(a,b,c,d)

        print(len(cache))
        return max_size






if __name__ == '__main__':
    # s = "abcde" 
    # t = "ecdba"
    # s = "b" 
    # t = "aaaa"
    s = "fotmotdhylkdksumrsgoqzxyhznkbwmpyuqjg"
    t = "fitaonugabwrlwinzohtgclebuvojhy"
    s = "cvnln"
    t = "ymjpbtv"
    r = Solution().longestPalindrome(s,t)
    print('r: ',r)

    


        
        
            


        

        