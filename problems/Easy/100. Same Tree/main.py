from typing import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def bfs(start_point):
            visited = set()
            queue = [start_point]
            res = []
            while queue: 
                node = queue.pop(0)
                if node not in visited:
                    if node:
                        visited.add(node)
                        res.append(node.val)
                        if node.left or node.right:
                            queue.append(node.left)
                            queue.append(node.right)
                    else:
                        res.append(None)
            return res
        r1 = bfs(p)
        r2 = bfs(q)
        print(r1,r2)
        if len(r1) != len(r2):
            return False 
        for i in range(len(r1)):
            if r1[i] != r2[i]:
                return False 
        return True

## recursive
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)


if __name__ == '__main__':
    p = TreeNode(1,None,TreeNode(2,TreeNode(3),None))
    q = TreeNode(1,None,TreeNode(2,None,TreeNode(3)))
    r = Solution().isSameTree(p,q)
    print(r)
