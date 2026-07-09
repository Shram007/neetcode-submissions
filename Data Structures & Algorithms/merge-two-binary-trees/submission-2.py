# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1: return root2
        if not root2: return root1

        root = TreeNode(root1.val + root2.val)
        stack = [(root1, root2, root)]

        while stack:
            node1, node2, node = stack.pop()

            if node1.left and node2.left:
                node.left = TreeNode(node1.left.val + node2.left.val)
                stack.append((node1.left, node2.left, node.left))
            elif not node1.left:
                node.left = node2.left
            else:
                node.left = node1.left
            
            if node1.right and node2.right:
                node.right = TreeNode(node1.right.val + node2.right.val)
                stack.append((node1.right, node2.right, node.right))
            elif not node1.right:
                node.right = node2.right
            else:
                node.right = node1.right

        return root