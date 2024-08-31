#pip install anytree
from anytree import Node, RenderTree

# Create the tree structure
root = Node("A")
b = Node("B", parent=root)
c = Node("C", parent=root)
d = Node("D", parent=b)
e = Node("E", parent=b)
e2 = Node("E2", parent=b)
f = Node("F", parent=c)
g = Node("G", parent=c)
h = Node("H", parent=e)
i = Node("I", parent=e)

# Render the tree
print("Tree Structure:")
for pre, _, node in RenderTree(root):
    print(f"{pre}{node.name}")