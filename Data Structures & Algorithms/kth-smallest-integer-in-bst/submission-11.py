# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        curr = root

        # When current and stack is not null
        while curr or stack:
            # Keep going left
            while curr:
                stack.append(curr)
                curr = curr.left
            # Current at null => pop most recent added element
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            # Go to current right child now
            curr = curr.right