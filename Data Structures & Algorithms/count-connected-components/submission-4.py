class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1
            while res != par[res]:       #while result is not its own parent, not default
                par[res] = par[par[res]] #Path compression
                res = par[res]
            return res
    
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:                #If same parent => already merged
                return 0
            if rank[p2] > rank[p1]:     #If p2 part of larger union branch
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1
        
        result = n
        for node1, node2 in edges:
            result -= union(node1, node2)
        return result

