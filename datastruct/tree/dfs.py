class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
def create_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(9)
    root.left.right.left = TreeNode(10)
    root.left.right.right = TreeNode(11)
    return root
def print_tree(root):
    def dfs(node):
        if not node:
            return 
        print(node.val)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
root = create_tree()

def dfs(graph,node,visited=set(),path=[]):
    # if node in visited:
    #     return 
    if node is None:
        # print(path)
        return
    visited.add(node)
    path.append(node.val)
    if node.val == 10:
        print(path)
    dfs(graph,node.left,visited,[*path])
    dfs(graph,node.right,visited,[*path])

dfs(root,root)