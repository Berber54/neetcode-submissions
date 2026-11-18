# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def maxDepth(node):
            if not node:
                return 0
            return 1 + max(maxDepth(node.left), maxDepth(node.right))
        
        def helper(node):
            res = float('-inf')
            res = max(res, maxDepth(node.left) + maxDepth(node.right))
            if node.left:
                res = max(res, helper(node.left))
            if node.right:
                res = max(res, helper(node.right))
            return res
        
        return helper(root)