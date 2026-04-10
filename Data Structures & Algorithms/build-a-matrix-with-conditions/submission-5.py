class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:

        def buildOrder(conditions):   
            adj = defaultdict(list)
            indegree = defaultdict(int)
            for src, dst in conditions:
                adj[src].append(dst)
                indegree[dst] += 1
            
            q = deque()
            order = {}
            index = 0
            for i in range(1, k + 1):
                if indegree[i] == 0:
                    q.append(i)
            
            while q:
                curr = q.popleft()
                order[curr] = index
                for nei in adj[curr]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)
                index += 1
            if index != k:
                return []
            return order
        
        rowOrder = buildOrder(rowConditions)
        colOrder = buildOrder(colConditions)
        if not rowOrder or not colOrder:
            return []

        res = [[0] * k for _ in range(k)]
        for i in range(1, k + 1):
            row, col = rowOrder[i], colOrder[i]
            res[row][col] = i
        return res