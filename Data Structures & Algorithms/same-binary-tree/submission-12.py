# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both trees are null, equal => True
        if not p and not q:
            return True
        # One tree null other not, equal => False
        if not p and q or p and not q:
            return False
        # If value of root node different => False
        if p.val != q.val:
            return False
        # Root nodes are same, check if left/right are the same
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)