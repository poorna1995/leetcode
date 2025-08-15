class TreeNode:
    def __init__(self):
        self.val = val
        self.left = None
        self.right = None
        
        
        


class DFS:
    def __init__(self):
        self.root = None
    
    
    def pre_order(self,root):
        stack = [root]
        result = []
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result