# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        x = deque([p])
        y = deque([q])
        while x and y:
            xtemp = x.popleft()
            ytemp = y.popleft()
            if xtemp and ytemp:
                if xtemp.val != ytemp.val:
                    return False
            else:
                if xtemp and not ytemp:
                    return False
                elif ytemp and not xtemp:
                    return False

            if xtemp:
                x.extend([xtemp.left, xtemp.right])
            if ytemp:
                y.extend([ytemp.left, ytemp.right])

        return True