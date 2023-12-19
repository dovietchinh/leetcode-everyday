class Solution(object):
    def longestValidParentheses(self, s):
        count = 0
        max_value = 0
        size = len(s)
        for i in range(1,size):
            current = s[i]
            old = s[i-1]
            if old == ')' and current == '(':
                continue
            if old=='(' and current ==')':
                count += 1
                max_value = max(max_value,count)
            if old==current:
                count = 0 
                max_value = max(max_value,count)
        return max_value *2
                
            
            



if __name__ == '__main__':
    pass