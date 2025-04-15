class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root:TreeNode):
    if root==None:
        return 0
    return 1+max(maxDepth(root.left),maxDepth(root.right))


print(maxDepth(TreeNode(val = 1, left= TreeNode(val = 2), right= None)))