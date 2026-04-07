class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = [set() for _ in range(n + 1)]
        outdegree = [set() for _ in range(n + 1)]
        for src, dst in trust:
            indegree[dst].add(src)
            outdegree[src].add(dst)
        
        for i in range(1, n + 1):
            if len(indegree[i]) == n - 1 and len(outdegree[i]) == 0:
                return i

        return -1