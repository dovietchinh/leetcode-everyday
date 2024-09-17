from typing import *
class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        size = len(s)
        word = ''
        for j in range(size-1,-1,-1):
            if j == 0:
                if s[j]!= " ":
                    stack.append(s[j])
                if stack:
                    if word != "":
                        word += ' '
                    word += ''.join(stack[::-1])
                    stack.clear()
                break 
            else:
                if s[j]!= ' ':
                    stack.append(s[j])
                else:
                    if stack:
                        if word != "":
                            word += ' '
                        word += ''.join(stack[::-1])
                        stack.clear()
        return word

        



if __name__ == '__main__':
    r = Solution().reverseWords("alsdhaslkd")
    print('answer:',r)
    print(r=="alsdhaslkd")
    