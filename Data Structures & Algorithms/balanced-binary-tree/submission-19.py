# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr, depth):
            if not curr:
                return depth
            
            depth = max(dfs(curr.left, depth + 1), dfs(curr.right, depth + 1))
            return depth
        def helper(curr):
            if not curr:
                return True
            left = dfs(curr.left, 0)
            right = dfs(curr.right, 0)
            
            if abs(left - right) > 1:
                return False
            return helper(curr.left) and helper(curr.right)
        return helper(root)