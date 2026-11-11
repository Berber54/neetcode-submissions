# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.q = deque([root])
        self.res = []

        def helper():
            r = []
            if not self.q:
                return
            level_size = len(self.q)
            for x in range(level_size):
                tmp = self.q.popleft()
                if not tmp:
                    return
                r.append(tmp.val)
                if tmp.left:
                    self.q.append(tmp.left)
                if tmp.right:
                    self.q.append(tmp.right)
            self.res.append(r)
            return helper()
        helper()
        return self.res
