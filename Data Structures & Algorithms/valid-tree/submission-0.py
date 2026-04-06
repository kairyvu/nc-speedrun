class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        adj = [[] for _ in range(n)]
        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        
        q = deque([0])
        visited = set()
        visited.add(0)
        
        while q:
            edge = q.popleft()
            for nei in adj[edge]:
                if nei not in visited:
                    q.append(nei)
                    visited.add(nei)
        
        return len(visited) == n