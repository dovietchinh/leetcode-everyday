# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
class Solution:
    def intToRoman(self, num: int) -> str:
        a = num // 1000
        b = num %1000 // 100
        c = num %100 //10
        d = num %10
        r = ''
        r += 'M' * a
        r += ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM'][b]
        r += ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC'][c]
        r += ['','I','II','III','IV','V','VI','VII','VIII','IX'][d]
        return r


if __name__ == '__main__':
    for _ in range(100):
        import random 
        i = random.randint(0,4000)
        r = Solution().intToRoman(i)
        print(i," : ",r)
        
