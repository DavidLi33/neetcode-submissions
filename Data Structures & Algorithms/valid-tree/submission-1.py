class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True
        
        adj = { i:[] for i in range(n)}
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        
        visit = set()
        def dfs(i, prev):
            if i in visit:
                return False
            visit.add(i)
            for neighbor in adj[i]:
                if neighbor == prev: 
                    continue
                if not dfs(neighbor, i):
                    return False
            return True

        return dfs(0, -1) and len(visit) == n
            
