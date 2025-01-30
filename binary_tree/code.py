class BSTNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        
    def print(self,key):
        print(self.key)
    
class BSTTree:
    def __init__(self):
        self.root = None
        
        
    def insert(self,key):
        new_node = key
        if self.root == None:
            self.root = new_node
        else:
            self._insert(self.root,new_node)
    def _insert(self,node,new_node):
        if new_node.key < node.key:
            if node.left is None:
                node.left = new_node
            else:
                self._insert(node.left, new_node)
        else:
            if node.right is None:
                node.right = new_node
            else:
                self._insert(node.right, new_node)
    

node = BSTNode(10)

