class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)

        visited = set()
        
        def dfs(node):
            for nei in adj[node]:
                if nei in visited:
                    continue
                visited.add(nei)
                dfs(nei)
        
        res = 0
        for e in range(n):
            if e not in visited:
                dfs(e)
                res += 1
        return res