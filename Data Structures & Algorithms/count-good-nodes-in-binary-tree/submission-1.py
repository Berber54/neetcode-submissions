# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = []

        def helper(node, prev_largest):
            if not node:
                return

            if node.val >= prev_largest:
                res.append(node.val)
                prev_largest = node.val
            
            helper(node.left, prev_largest)
            helper(node.right, prev_largest)

        helper(root, float('-inf'))
        return len(res)