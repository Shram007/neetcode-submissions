# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # morris traversal
        curr = root
        while curr:
            # No left child
            if not curr.left:
                k -= 1
                if k == 0:
                    return curr.val
                curr = curr.right
            # If left child, find right most node in left subtree
            else:
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right
                
                # when right child is Null, create a temp link between left child and curr
                if not pred.right:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    k -= 1
                    if k == 0:
                        return curr.val
                    curr = curr.right
        return -1


