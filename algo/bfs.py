# level order travasl


# use queue to traverse the graph


class TreeNode:
    def __init__(self):
        self.val = val
        self.left = None
        self.right = None
        

class BFS:
    def __init__(self, root):
        self.root = root
        
    
    def level_traversal(self):
        if not self.root:
            return []
        
        queue = [root]
        result = []
        
        while queue:
            node = queue.pop(0)
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result
    

    
    