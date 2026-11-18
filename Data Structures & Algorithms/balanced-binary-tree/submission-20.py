# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def maxDepth(node):
            if not node:
                return 0
            return 1 + max(maxDepth(node.left), maxDepth(node.right))

        def helper(node):
            if not node:
                return True
            if abs(maxDepth(node.left) - maxDepth(node.right)) > 1:
                return False
            return helper(node.left) and helper(node.right)

        return helper(root)