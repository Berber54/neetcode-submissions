# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(r, s):
            if not r and not s:
                return True
            if not s or not r or r.val != s.val:
                return False
            return isSameTree(r.left, s.left) and isSameTree(r.right, s.right)

        c = deque([root])
        while c:
            x = c.popleft()
            if not x:
                continue
            if x.val == subRoot.val:
                if isSameTree(x, subRoot):
                    return True
            c.extend([x.left, x.right])
        return False 