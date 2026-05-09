# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            # Null Case
            if not node:
                return True
            # If node.val not in left and right boundary bounds from parents
            if not(node.val < right and node.val > left):
                return False
            # Use node.val for right boundary on left child and vice versa
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        
        return valid(root, float('-inf'), float('inf'))