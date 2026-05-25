"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Base case 
        # Hashmap to store list of neighbors for each node
        # If node not exist, create copy
        # add copy of neighbors
        if not node:
            return None
        
        node_map = {}
        def dfs(node):
            if node in node_map:
                return node_map[node]
            node_copy = Node(node.val)
            node_map[node] = node_copy
            for neighbor in node.neighbors:
                node_copy.neighbors.append(dfs(neighbor))
            return node_map[node]
        return dfs(node)