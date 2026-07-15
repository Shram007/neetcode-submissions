# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, False)]
        depths = {None : 0}
        while stack:
            node, seen = stack.pop()
            # early exit for null nodes
            if node is None:
                continue
            if not seen:
                stack.append((node, True))
                stack.append((node.left, False))
                stack.append((node.right, False))
            else:
                l, r = depths[node.left], depths[node.right]
                if abs(l - r) > 1: return False
                depths[node] = 1 + max(l, r)
        return True

