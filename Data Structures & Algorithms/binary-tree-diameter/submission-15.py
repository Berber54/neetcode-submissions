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
            return 1 + max(maxDepth(node.right), maxDepth(node.left))

        def helper(node):
            res = 0
            if not node:
                return res
            res = max(maxDepth(node.left) + maxDepth(node.right), res)
            if node.left:
                res = max(helper(node.left), res)
            if node.right:
                res = max(helper(node.right), res)
            print(res)
            return res

        return helper(root)