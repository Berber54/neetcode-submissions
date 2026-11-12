# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        index = 1
        res = None
        def dfs(curr):
            nonlocal index, res
            if not curr:
                return
            dfs(curr.left)
            if res != None:
                return
            if index == k:
                res = curr.val
                return
            index += 1
            dfs(curr.right)
            return
        dfs(root)
        return res