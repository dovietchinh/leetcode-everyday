from typing import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = [[root,0]]
        while queue:
            node,level = queue.pop(0)
            if node is None:
                continue 
            else:
                if len(res) < level+1:
                    res.append([])
                res[level].append(node.val)
                queue.append([node.left,level+1])
                queue.append([node.right,level+1])
        res.reverse()   
        return res
        
if __name__ == '__main__':
    root = TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))
    r = Solution().levelOrderBottom(root)
    print(r)

