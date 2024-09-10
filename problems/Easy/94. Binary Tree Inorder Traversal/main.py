from typing import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def traversal(node):
            nonlocal res
            if node:
                traversal(node.left)
                res.append(node.val)
                traversal(node.right)
        traversal(root)
        return res

                



            
            



if __name__ == '__main__':
    root = TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5,TreeNode(6),TreeNode(7))),TreeNode(3,None,TreeNode(8,TreeNode(9))))
    r = Solution().inorderTraversal(root)
    print(r)