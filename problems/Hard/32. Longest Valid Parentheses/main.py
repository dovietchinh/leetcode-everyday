class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_length = 0
        stack = [-1]  # Initialize with a start index

        for i in range(len(s)):

            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)  # If popped -1, add a new start index
                else:
                    # Update the length of the valid substring
                    print('max_length: ',max_length)
                    print('i - stack[-1]: ',i - stack[-1])
                    max_length = max(max_length, i - stack[-1])
            print('i,stack: ',i,stack)
        return max_length

                
                

                
            
            



if __name__ == '__main__':
    r = Solution().longestValidParentheses(")()))()()())")
    print(r)