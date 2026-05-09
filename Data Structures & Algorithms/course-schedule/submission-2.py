class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        my_map = { i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            my_map[course].append(prereq)

        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if my_map[crs] == []:
                return True

            visited.add(crs)
            for prereq in my_map[crs]:
                if not dfs(prereq):
                    return False
            visited.remove(crs)
            my_map[crs] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
        