class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_map = {}
        for i in range(numCourses):
            prereq_map[i] = []

        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)

        course_set = set()
        def dfs(course):
            if course in course_set:
                return False
            if prereq_map[course] == []:
                return True

            course_set.add(course)
            for prereq in prereq_map[course]:
                if not dfs(prereq):
                    return False
            
            # If no issues, we remove since not visiting
            course_set.remove(course)
            prereq_map[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True