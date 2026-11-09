# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(curr, sub):
            if not sub and not curr:
                return True
            if not curr or not sub:
                return False
            if sub.val != curr.val:
                return False
            return isSameTree(curr.left, sub.left) and isSameTree(curr.right, sub.right)
        def traverse(curr, sub):
            if not sub:
                return True
            if not curr:
                return False
            if sub.val == curr.val:
                if isSameTree(curr, sub):
                    return True
            return traverse(curr.left, sub) or traverse(curr.right, sub)
        curr = root
        sub = subRoot
        return traverse(curr, sub)