# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If subRoot null => True by default
        if not subRoot:
            return True
        # If root null => False
        if not root:
            return False
        # If root same tree as subRoot => True
        if self.sameTree(root, subRoot):
            return True
        # See if left/right branch is same tree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Both null => True
        if not root and not subRoot:
            return True
        # One null and other not => False
        if not root and subRoot or root and not subRoot:
            return False
        # Different root valeus => False
        if root.val != subRoot.val:
            return False
        # Ensure left and right branches are the sameTree
        return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
