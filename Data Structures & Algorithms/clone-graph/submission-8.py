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
            # Clone of node already exists
            if node in my_map:
                return my_map[node]
            # Clone doesn't exist => Create copy of node
            copy_node = Node(node.val)
            # Add copy to hashmap
            my_map[node] = copy_node
            # Add copy of every single neighbor
            for neighbor in node.neighbors:
                copy_node.neighbors.append(dfs(neighbor))
            return my_map[node]
        
        return dfs(node)