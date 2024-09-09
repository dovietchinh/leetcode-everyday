class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        prev = 0
        path += '/'
        for index in range(1,len(path)):
            if path[index] == '/':
                name = path[prev+1:index]
                name = name.strip('/')
                if len (name) == 0:
                    pass
                elif name == '.':
                    pass 
                elif name == '..':
                    if stack:
                        stack.pop()
                else:
                    stack.append(name)
                prev = index

        # print('stack: ',stack)
        r = '/'.join(stack)
        return '/' + r
            
                



if __name__ == '__main__':
    p = "/.../a/../b/c/../d/./"
    p ="/home//foo/"
    p = "/home/user/Documents/../Pictures"
    r = Solution().simplifyPath(p)
    print(r)