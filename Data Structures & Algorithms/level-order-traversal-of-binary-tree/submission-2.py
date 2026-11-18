# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.q = deque([root])
        self.res = []
        def helper():
            r = []
            count = len(self.q)
            if count == 0:
                return
            for _ in range(count):
                tmp = self.q.popleft()
                if not tmp:
                    continue
                r.append(tmp.val)
                self.q.append(tmp.left)
                self.q.append(tmp.right)
            if r:
                self.res.append(r)
            return helper()
        helper()
        return self.res