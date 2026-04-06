class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        adj = [[] for _ in range(n)]
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        q = deque([0])
        visited = set()
        visited.add(0)
        
        while q:
            node = q.popleft()
            for nei in adj[node]:
                if nei not in visited:
                    q.append(nei)
                    visited.add(nei)
        
        return len(visited) == n