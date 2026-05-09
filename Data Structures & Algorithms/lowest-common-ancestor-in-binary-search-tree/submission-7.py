# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root

        # Keep searching to find lowest ancestor, not first ancestor
        while curr:
            # If both values greater, search right
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # If both values smaller, search left
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # Not same sign, return since best solution
            else:
                return curr
        