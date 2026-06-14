# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: return "$#"
        return ("$" + str(root.val) + self.serialize(root.left) + self.serialize(root.right))
    
    def z_function(self, s: str) -> list:
        z = [0] * len(s)
        l, r, n = 0, 0, len(s)
        for i in range(1, n):
            if i <= r:
                z[i] = min(r - i + 1, z[i - 1])
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            
            if i + z[i] - 1 > r:
                l, r = i, i + z[i] - 1

        return z

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        S_root = self.serialize(root)
        S_subRoot = self.serialize(subRoot)
        combined = S_subRoot + "|" + S_root

        z_vals = self.z_function(combined)
        sub_len = len(S_subRoot)

        for i in range(sub_len + 1, len(combined)):
            if z_vals[i] == sub_len:
                return True
        return False