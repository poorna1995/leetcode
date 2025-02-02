# three sum 

class BSTNode:
    def __init__(self,key):
        self.key   = key
        self.left  = None
        self.right = None

class SumBFS:
    def BFS(self,root):
        if root is None:
            return 0
        
        queue = [root]
        total_sum = 0
        
        while queue:
            node = queue.pop(0)
            total_sum += node.key
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return total_sum


root = BSTNode(1)
root.left = BSTNode(2)
root.right = BSTNode(3)
root.left.left = BSTNode(4)
root.left.right = BSTNode(5)
root.right.left = BSTNode(6)
root.right.right = BSTNode(7)


sum = SumBFS()
result= sum.BFS(root)
print(result)





# DFS

class SumDFS:
    def DFS(self, root):
        if root is None:
            return 0
        return root.key + self.DFS(root.left) + self.DFS(root.right)
    
    


root = BSTNode(10)
root.left = BSTNode(5)
root.right = BSTNode(15)
root.left.left = BSTNode(3)
root.left.right = BSTNode(7)


sum_dfs = SumDFS()
output = sum_dfs.DFS(root)
print("Sum of all nodes:", output)  # Output: Sum of all nodes: 40
