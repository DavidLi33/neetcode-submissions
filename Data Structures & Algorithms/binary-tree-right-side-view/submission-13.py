# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()
        q.append(root)

        # BFS approach
        while q:
            # Initialize right node at current level
            right_node = None
            for i in range(len(q)):
                curr_node = q.popleft()
                # Continuously update right_node for each curr_node being popped
                if curr_node:
                    right_node = curr_node
                    q.append(curr_node.left)
                    q.append(curr_node.right)
            # Only append value if right_node is not null
            if right_node:
                res.append(right_node.val)
        return res