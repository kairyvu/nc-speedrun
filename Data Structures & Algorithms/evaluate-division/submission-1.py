class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (a, b), value in zip(equations, values):
            graph[a][b] = value
            graph[b][a] = 1 / value
        
        for var in graph:
            for a in graph[var]:
                for b in graph[var]:
                    if b not in graph[a]:
                        graph[a][b] = graph[a][var] * graph[var][b]
        
        res = []
        for a, b in queries:
            if a in graph and b in graph[a]:
                res.append(graph[a][b])
            else:
                res.append(-1)
        return res