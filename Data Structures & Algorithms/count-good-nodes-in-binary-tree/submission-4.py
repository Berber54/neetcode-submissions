# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, curr_largest):
            if not node:
                return 0
            
            good = int(node.val >= curr_largest)
            curr_largest = max(node.val, curr_largest)

            return good + dfs(node.left, curr_largest) + dfs(node.right, curr_largest)

        return dfs(root, float('-inf'))