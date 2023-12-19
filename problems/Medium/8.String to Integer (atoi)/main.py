class Solution:
    def myAtoi(self, s: str) -> int:
        num = ''
        state = 0
        a = 1
        for i in s:
            if state == 0:
                if i==' ':
                    continue
                elif i=='+':
                    state = 1
                    continue
                elif i=='-':
                    a = -1
                    state = 1
                    continue
                elif ord('0') <= ord(i) <= ord('9'):
                    num += i
                    state = 2 
                else:
                    break
            elif state == 1:
                if ord('0') <= ord(i) <= ord('9'):
                    num += i
                    state = 2
                else:
                    break
            elif state == 2:
                if ord('0') <= ord(i) <= ord('9'):
                    num += i
                else:
                    break
            else:
                break
        if len(num)==0:
            return 0
        r = a*int(num)
        return max(min(2**31-1,r),-2**31)
                
            
            
if __name__ == '__main__':
    r = Solution().myAtoi('  +-123543 ')
    print(r)
            
        

            

