from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        root.left, root.right = root.right, root.left
        # print(root.left)
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        

solution = Solution()
root = [4,2,7,1,3,6,9]
print(solution.invertTree(root))




# root = [4,2,7,1,3,6,9]

