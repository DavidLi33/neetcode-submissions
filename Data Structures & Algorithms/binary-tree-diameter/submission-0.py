# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Create global variable to update the max diameter
        self.res = 0

        # DFS returns height, not diameter
        def dfs(curr):
            if not curr:
                return 0
            
            # Get height for left and right branch
            left = dfs(curr.left)
            right = dfs(curr.right)

            # Update largest diameter
            self.res = max(self.res, left + right)
            return 1 + max(left, right)
        
        # Call DFS on initial root
        dfs(root)
        return self.res
