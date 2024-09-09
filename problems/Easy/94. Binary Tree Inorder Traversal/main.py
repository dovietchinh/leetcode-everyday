from typing import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        stack = []
        def dfs(node,level):
            nonlocal stack
            if node:
                stack.append([node.val,level])
                dfs(node.right, level + 1)
                dfs(node.left,level -1)
        dfs(root,0)
        stack.sort(key=lambda x: x[1])
        print('stack: ',stack)
        # return stack[::-1]

                



            
            



if __name__ == '__main__':
    root = TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5,TreeNode(6),TreeNode(7))),TreeNode(3,None,TreeNode(8,TreeNode(9))))
    r = Solution().inorderTraversal(root)
    print(r)