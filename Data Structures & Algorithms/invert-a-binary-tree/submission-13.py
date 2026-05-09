# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case
        if not root:
            return None
        
        # Swap initial left and right children
        temp = root.left
        root.left = root.right
        root.right = temp

        # Recurse on left and right children of the left and right branches
        # Need to call self.invertTree since we are in the function invertTree
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
