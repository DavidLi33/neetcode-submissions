"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        my_map = {}

        def dfs(node):
            if node in my_map:
                return my_map[node]
            copy_node = Node(node.val)
            my_map[node] = copy_node
            for neighbor in node.neighbors:
                copy_node.neighbors.append(dfs(neighbor))
            return my_map[node]
        
        return dfs(node)