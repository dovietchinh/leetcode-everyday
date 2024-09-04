from typing import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.val)

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check_2_tree(p,q):
            # print(p,q)
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                # print(p.val,q.val)
                return False 
            return check_2_tree(p.left,q.right) and check_2_tree(p.right,q.left)
        return check_2_tree(root.left,root.right)
            
            


if __name__ == '__main__':
    root = TreeNode(1,TreeNode(2,TreeNode(3),TreeNode(4)),TreeNode(2,TreeNode(4),TreeNode(3)))
    root = TreeNode(1,TreeNode(2,None,TreeNode(3)),TreeNode(2,None,TreeNode(3)))
    r = Solution().isSymmetric(root)
    print(r)
