from typing import *
# Definition for a binary tree node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        queue = [[root,0]]
        current_level = 0 
        res = []
        while queue:
            node,level = queue.pop(0)
            if node is None:
                continue
            # print(node.val)
            if level > current_level:
                current_level = level
                # print('#')
                # print(node.val)
                
            else:
                if len(res) > 0:
                    res[-1].next = node
                    # print(node.val)
            res.append(node)
            queue.append([node.left,level+1])
            queue.append([node.right,level+1])
        return root
if __name__ == '__main__':
    root = Node(1,Node(2,Node(4),Node(5)),Node(3,None,Node(7)))
    r = Solution().connect(root)
    # print(r)

