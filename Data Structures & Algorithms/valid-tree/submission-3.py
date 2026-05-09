class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True

        adj = defaultdict(list)
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        
        visit = set()
        def dfs(i, prev):
            # Loop detected
            if i in visit:
                return False
            visit.add(i)
            # Search through neighbors
            for neighbor in adj[i]:
                # Prevent false loop detection of 0 -> 1 and 1 -> 0
                if neighbor == prev: 
                    continue
                # Loop detected if dfs is false
                if not dfs(neighbor, i):
                    return False
            return True

        return dfs(0, -1) and len(visit) == n
            
