from typing import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def insert(root,val):
            if root.val == 0:
                root.val = val
                return root 
            else:
                if val < root.val:
                    if root.left is None:
                        root.left = TreeNode(val)
                    else:
                        insert(root.left,val)
                elif val > root.val:
                    if root.right is None:
                        root.right = TreeNode(val)
                    else:
                        insert(root.right,val)
            return root 

        permutaions = []
        def permutation_array(arr,tail):
            if len(arr) == 0:
                permutaions.append(tail)
            for i in range(len(arr)):
                permutation_array(arr[:i]+arr[i+1:],[*tail,array[i]])
        array = list(range(1,n+1))
        permutation_array(array,[])

        list_tree = []
        for j in permutaions:
            root = TreeNode(0)
            for i in j:
                insert(root,i)
            list_tree.append(root)
        return list_tree
            
            

                    
def insert(root,val):
    if root.val == 0:
        root.val = val
        return root 
    else:
        if val < root.val:
            if root.left is None:
                root.left = TreeNode(val)
            else:
                insert(root.left,val)
        elif val > root.val:
            if root.right is None:
                root.right = TreeNode(val)
            else:
                insert(root.right,val)
    # return root 


def backtracking(root,stack=[]):
    unvisited = []
    
def combination(n,stack=[]):
    if len(stack) == 2:
        print(stack)
        return
    for i in range(len(n)):
        a(n[:i]+n[i+1:],[*stack,n[i]])


def combinations(arr, r):
    result = []
    
    def backtrack(start, path):
        # If the combination is of the desired length, add to result
        if len(path) == r:
            result.append(path)
            return
        
        for i in range(start, len(arr)):
            # Include arr[i] in the combination and move to the next element
            backtrack(i + 1, path + [arr[i]])    
    backtrack(0, [])
    return result


if __name__ == '__main__':
    # # root = TreeNode(1,TreeNode(0),TreeNode(2,None,TreeNode(4,None,TreeNode(5))))
    # # insert(root,6)
    # # r = root 
    # # queue = [r]
    
    # # while queue:
    # #     node = queue.pop(0)
    # #     print(node.val) if node else print(None)
    # #     if node:
    # #         queue.append(node.left)
    # #         queue.append(node.right)
    # root = TreeNode(0)
    # insert(root,1)
    # insert(root,2)
    # insert(root,3)
    # queue = [root]
    # while queue:
    #     node = queue.pop(0)
    #     print(node.val) if node else print(None)
    #     if node:
    #         queue.append(node.left)
    #         queue.append(node.right)

    # a([1,2,3,4],[])
    pass