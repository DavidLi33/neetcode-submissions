# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()

        # Base case
        if root:
            q.append(root)
        
        # BFS approach
        while q:
            # Store level for each for loop through q
            level = []
            curr_len = len(q)
            for i in range(curr_len):
                # Pop current node
                node = q.popleft()

                # Add value to level list
                level.append(node.val)
                # Add left/right children in order
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # Add level values to overall result list
            res.append(level)
        return res