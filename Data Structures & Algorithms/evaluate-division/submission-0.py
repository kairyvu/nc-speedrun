class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i in range(len(equations)):
            adj[equations[i][0]].append((equations[i][1], values[i]))
            adj[equations[i][1]].append((equations[i][0], 1 / values[i]))
        
        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1
            
            q = deque([(src, 1)])
            visited = set([src])
            while q:
                node, val = q.popleft()
                if node == target:
                    return val
                for nei, div in adj[node]:
                    if nei in visited:
                        continue
                    visited.add(nei)
                    q.append((nei, val * div))
            return -1
        
        res = []
        for q0, q1 in queries:
            res.append(bfs(q0, q1))
        return res