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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        step = 0 
        min_depth = float('inf')        
        queue = [[root,step]]
        while queue: 
            node,step = queue.pop(0)
            if node is None:
                if step < min_depth:
                    min_depth = step
                continue
            else:
                queue.append([node.left,step+1])
                queue.append([node.right,step+1])   
        return min_depth
    



            
            


if __name__ == '__main__':
    root = TreeNode(2,None,TreeNode(3,None,TreeNode(4,None,TreeNode(5,None,TreeNode(6)))))
    # root = TreeNode(1,None,TreeNode(2))
    r = Solution().minDepth(root)
    print(r)
