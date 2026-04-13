class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [i for i in range(n)]
        self.ranks = [1] * n

    def find(self, x):
        while self.parents[x] != x:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        return self.parents[x]
    
    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return False
        self.n -= 1
        if self.ranks[p1] < self.ranks[p2]:
            self.parents[p1] = p2
            self.ranks[p2] += self.ranks[p1]
        else:
            self.parents[p2] = p1
            self.ranks[p1] += self.ranks[p2]
        return True
    
    def isConnected(self):
        return self.n == 1

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        uf = UnionFind(len(nums))
        factors = {}

        for i, num in enumerate(nums):
            currFactor = 2
            while currFactor * currFactor <= num:
                if num % currFactor == 0:
                    if currFactor in factors:
                        uf.union(i, factors[currFactor])
                    else:
                        factors[currFactor] = i
                    while num % currFactor == 0:
                        num //= currFactor
                currFactor += 1
            if num > 1:
                if num in factors:
                    uf.union(i, factors[num])
                else:
                    factors[num] = i
        return uf.isConnected()












        