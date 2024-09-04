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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        current = 0
        max_step = 0
        def get_max_step(node,current):
            nonlocal max_step
            if node is None:
                if current > max_step:
                    max_step = current
                return 
            get_max_step(node.left,current+1)
            get_max_step(node.right,current+1)
        get_max_step(root,current)
        return max_step

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ## bfs 
        current = 0 
        max_depth = 0
        queue = [[root,current]]
        while queue:
            node,current = queue.pop(0)
            if node is None:
                if current > max_depth:
                    max_depth = current
                continue
            else:
                # print('node: ', node.val)
                queue.append([node.left,current+1])
                queue.append([node.right,current+1])
        return max_depth



            
            


if __name__ == '__main__':
    root = TreeNode(1,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))
    # root = TreeNode(1,None,TreeNode(2))
    r = Solution().maxDepth(root)
    print(r)
