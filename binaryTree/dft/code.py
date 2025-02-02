class BSTNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

class DepthFirstTraversal:
    def dft(self,root):
        if root is None:
            return []
        stack = [root]
        values = []
        while stack:
            node = stack.pop()
            values.append(node.key)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return values





root = BSTNode(10)
root.left = BSTNode(5)
root.right = BSTNode(15)
root.left.left = BSTNode(3)
root.left.right = BSTNode(7)
root.right.left = BSTNode(12)
root.right.right = BSTNode(18)

df = DepthFirstTraversal()
result = df.dft(root)
print(result)