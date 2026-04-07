class DSU:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, x):
        while x != self.parents[x]:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        return x
    
    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return False
        elif self.rank[p1] < self.rank[p2]:
            self.parents[p1] = p2
            self.rank[p2] += self.rank[p1]
        else:
            self.parents[p2] = p1
            self.rank[p1] += self.rank[p2]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        unionFind = DSU((len(accounts)))
        emailToAccount = {}

        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                if account[j] in emailToAccount:
                    unionFind.union(i, emailToAccount[account[j]])
                else:
                    emailToAccount[account[j]] = i
        
        emailGroup = defaultdict(list)
        for email, index in emailToAccount.items():
            parent = unionFind.find(index)
            emailGroup[parent].append(email)
        
        res = []
        for index, emails in emailGroup.items():
            account = accounts[index][0]
            emails.sort()
            res.append([account] + emails)
        return res