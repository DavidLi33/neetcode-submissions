# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            # No node is balanced by default
            # True indicates if it is balanced and 0 indicates height
            if not root:
                return [True, 0]
            
            # Run dfs on left/right child
            left, right = dfs(root.left), dfs(root.right)

            # Check if heights are balanced and if left/right are both True
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            # Return balanced bool value and current height
            return [balanced, 1 + max(left[1], right[1])]

        # Return bool value
        return dfs(root)[0]