from typing import List,Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def helper(root, res):
            if not root:
                return res
            helper(root.left, res)
            res.append(root.val)
            helper(root.right, res)
        
        helper(root, res)
        return res