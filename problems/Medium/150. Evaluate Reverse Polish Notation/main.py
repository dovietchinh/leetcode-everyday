from typing import *
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for index,token in enumerate(tokens):
            if token not in ["+","/","-","*"]:
                stack.append(int(token))
            else:
                if token == "+":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a+b)
                elif token == "-":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b-a)
                elif token == "*":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a*b)
                elif token == "/":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b/a))
        return stack[0]
if __name__ == '__main__':
    r = Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
    print(r)
    