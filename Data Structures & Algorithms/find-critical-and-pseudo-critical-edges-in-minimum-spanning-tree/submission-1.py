class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.ranks = [1] * n
    
    def find(self, v):
        while v != self.parents[v]:
            self.parents[v] = self.parents[self.parents[v]]
            v = self.parents[v]
        return self.parents[v]
    
    def union(self, u, v):
        p1, p2 = self.find(u), self.find(v)
        if p1 == p2:
            return False
        if self.ranks[p1] < self.ranks[p2]:
            self.parents[p1] = p2
            self.ranks[p2] += self.ranks[p1]
        else:
            self.parents[p2] = p1
            self.ranks[p1] += self.ranks[p2]
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, e in enumerate(edges):
            e.append(i)
        
        edges.sort(key=lambda e: e[2])
        mstWeight = 0
        uf = UnionFind(n)
        for u, v, weight, _ in edges:
            if uf.union(u, v):
                mstWeight += weight

        critical, pseudo = [], []
        for u1, v1, w1, i in edges:
            currMst = 0
            uf = UnionFind(n)
            for u2, v2, w2, j in edges:
                if i != j and uf.union(u2, v2):
                    currMst += w2

            if mstWeight < currMst or max(uf.ranks) != n:
                critical.append(i)
                continue
            
            currMst = w1
            uf = UnionFind(n)
            uf.union(u1, v1)
            for u2, v2, w2, _ in edges:
                if uf.union(u2, v2):
                    currMst += w2
            if currMst == mstWeight:
                pseudo.append(i)
        
        return [critical, pseudo]