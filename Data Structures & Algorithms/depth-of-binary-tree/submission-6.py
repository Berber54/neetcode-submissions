# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(root, n):
            if not root.left and not root.right:
                return n
            l = r = 0
            if root.left:
                l = helper(root.left, n + 1)
            if root.right:
                r = helper(root.right, n + 1)
            return max(l, r)
        return helper(root, 1) if root else 0