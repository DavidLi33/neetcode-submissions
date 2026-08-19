class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list) # node => [node]
        incoming = defaultdict(int) 

        for dst, src in prerequisites:
            adj_list[src].append(dst)
            incoming[dst] += 1
        
        q = deque()
        for src in range(numCourses):
            if incoming[src] == 0:
                q.append(src)
        
        count = 0
        while q:
            src = q.popleft()
            count += 1
            for dst in adj_list[src]:
                incoming[dst] -= 1
                if incoming[dst] == 0:
                    q.append(dst)
        
        return count == numCourses # No cycle
