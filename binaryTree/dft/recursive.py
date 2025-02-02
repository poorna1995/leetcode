class BSTNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

class DepthFirstTraversal:
    def recursiveDFT(self, root):
        if root is None:
            return []
    
        leftValues = self.recursiveDFT(root.left)
        rightValues = self.recursiveDFT(root.right)
        
        return [root.key, *leftValues, *rightValues]
