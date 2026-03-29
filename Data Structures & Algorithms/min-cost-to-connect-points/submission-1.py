class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n, index = len(points), 0
        dist = [float("inf")] * n
        visited = [False] * n
        edges, res = 0, 0

        while edges < n - 1:
            visited[index] = True
            nextNode = -1
            for i in range(n):
                if visited[i]:
                    continue
                currDist = abs(points[i][0] - points[index][0]) + abs(points[i][1] - points[index][1])
                dist[i] = min(dist[i], currDist)
                if nextNode == -1 or dist[i] < dist[nextNode]:
                    nextNode = i
            
            res += dist[nextNode]
            index = nextNode
            edges += 1
        
        return res