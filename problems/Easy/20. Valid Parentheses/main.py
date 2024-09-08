class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            elif i == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif i == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            elif i == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            else:
                return False
        if stack:
            return False
        else:
            return True
            

    
if __name__ == '__main__':
    s = Solution()
    print(s.isValid('()'))
    print(s.isValid('()[]{}'))
    print(s.isValid('(]'))
    print(s.isValid('([)]'))
    print(s.isValid('{[]}'))
