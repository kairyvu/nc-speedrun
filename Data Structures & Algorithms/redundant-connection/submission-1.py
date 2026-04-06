class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = [i for i in range(n + 1)]
        rank = [1] * (n + 1)

        def find(n):
            if n != parents[n]:
                parents[n] = find(parents[n])
            return parents[n]
            
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                parents[p2] = p1
                rank[p1] += rank[p2]
            else:
                parents[p1] = p2
                rank[p2] += rank[p1]

            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]