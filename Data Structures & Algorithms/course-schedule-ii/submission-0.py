class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = defaultdict(list)

        for c, pre in prerequisites:
            indegree[c] += 1
            adj[pre].append(c)
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        learned = []
        while q:
            course = q.popleft()
            learned.append(course)
            for nei in adj[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return learned if len(learned) == numCourses else []