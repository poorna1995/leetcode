


# val --> left --> right

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, val: int):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert(self.root, val)
        return self.root
    
    def _insert(self, current_node, val: int):
        # We assume current_node is never None when this is called
        if val <= current_node.val:
            if current_node.left is None:
                current_node.left = TreeNode(val)
            else:
                self._insert(current_node.left, val)
        else: # val > current_node.val
            if current_node.right is None:
                current_node.right = TreeNode(val)
            else:
                self._insert(current_node.right, val)
        return self.root
    
    
    def search(self, val):
        return self._search(self.root, val)

    def _search(self, current_node, val):
        if current_node is None:
            return False
        if current_node.val == val:
            return True
        elif val <= current_node.val:
            self._search(current_node.left, val)
        else:
            self._search(current_node.right, val)
        return False
    
    def delete(self, val):
        self.root = self._delete(self.root,val)
        
    
    def _delete(self, current_node, val):
        
        if not current_node:
            return None
    
        if val < current_node.val:
            self._delete (current_node.left, val)
        elif val > current_node.val:
            self._delete (current_node.right, val)
        else:
            if not current_node.left:
                return current_node.right
            elif not current_node.right:
                return current_node.left
            else:
                
                min_node = current_node.right
                while min_node.left:
                    min_node = min_node.left
                current_node.val = min_node.val
                self._delete(current_node.right, min_node.val)
        return node
    
    
    def getMin(self):
        curr = self.root
        while curr:
            curr = curr.left
        return curr.val if curr else None
    
    def getMax(self):
        curr = self.root
        while curr:
            curr = curr.right
        return curr.val if curr else None
    
    
        
        
        # case1 : if the root / currentnode is none retruen none
        # case2 : if the root vaue/ currentnode value doen;t have right value then inplace tje left node
        # caser3 : if the root value/ currentnode value doesn't have left value then inplace the right node
        # case 4 : if root doen;t has any left and right then remoce the root value
        # case 5 : if root value/ current value both has the left and right then find the min of the right side and delete the current vale and add the min calue to the current node
        

    def _preorder(self, node):
        if node:
            print(node.val, end=' ')
            self._preorder(node.left)
            self._preorder(node.right)
    
    def preorder_travasel(self):
        self._preorder(self.root)
    






if __name__ == "__main__":
    bst = BST()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    
    print(bst.root)
    print(bst.search(15))  # True
    print(bst.search(7))   # False
    print(bst.preorder_travasel()) 
