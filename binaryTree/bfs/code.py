class BSTNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
    

class BreadthFirstTraversal:
    def BFT(self,root):
        if root is None:
            return []
        values = []
        queue = [root]
        
        while queue:
            node = queue.pop(0)
            values.append(node.key)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return values




   

# Create the binary search tree (BST)
root = BSTNode(1)
root.left = BSTNode(2)
root.right = BSTNode(3)
root.left.left = BSTNode(4)
root.left.right = BSTNode(5)
root.right.left = BSTNode(6)
root.right.right = BSTNode(7)

# Perform Breadth-First Traversal
bft = BreadthFirstTraversal()
result = bft.BFT(root)
print(result)