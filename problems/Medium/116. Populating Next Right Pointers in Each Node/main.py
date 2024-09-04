from typing import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = [[root,0]]
        current_level = 0
        res = []
        while queue:
            node,level = queue.pop(0)
            if node is None:
                continue 
            if level > current_level:
                current_level = level
            else:
                if len(res)!=0:
                    res[-1].next = node
            res.append(node)

            queue.append([node.left,level+1])
            queue.append([node.right,level+1])
        return root
        
if __name__ == '__main__':
    root = TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5)),TreeNode(3,TreeNode(6),TreeNode(7)))
    r = Solution().connect(root)
    print(r)

