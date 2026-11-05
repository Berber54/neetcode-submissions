# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if not q and not p:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        def traverse(root, subRoot):
            if not root:
                return False
            if root.val == subRoot.val:
                if isSameTree(root, subRoot):
                    return True
            return traverse(root.left, subRoot) or traverse(root.right, subRoot)
        
        return traverse(root, subRoot)