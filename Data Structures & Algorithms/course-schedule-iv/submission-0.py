class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        preCourse = [set() for _ in range(numCourses)]
        for pre, c in prerequisites:
            preCourse[c].add(pre)
        
        visited = set()
        
        def dfs(course):
            if course in visited:
                return preCourse[course]
            visited.add(course)            
            for pre in list(preCourse[course]):
                allPre = dfs(pre)
                for c in allPre:
                    preCourse[course].add(c)
            return preCourse[course]

        for c in range(numCourses):
            if c not in visited:
                dfs(c)

        res = [False] * len(queries)
        for i, q in enumerate(queries):
            if q[0] in preCourse[q[1]]:
                res[i] = True
        
        return res
            