class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]
        adj = [[] for _ in range(n)]
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        leaves = deque()
        edgeCount = {}
        for node, nei in enumerate(adj):
            if len(nei) == 1:
                leaves.append(node)
            edgeCount[node] = len(nei)
        
        while leaves:
            if n <= 2:
                return list(leaves)
            for _ in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for nei in adj[node]:
                    edgeCount[nei] -= 1
                    if edgeCount[nei] == 1:
                        leaves.append(nei)