class Solution(object):
    def balancedStringSplit(self, s):
        r = 0
        c = 0
        for i in s:
            if i=='R':
                c += 1
            else:
                c -= 1
            if c==0:
                r += 1
        return r
    
    
    

if __name__ == '__main__':
    for i in ["RLRRLLRLRL","RLRRRLLRLL","LLLLRRRR"]:
        r = Solution().balancedStringSplit(i)
        print(r)
        