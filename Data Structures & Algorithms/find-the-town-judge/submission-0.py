class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) != n - 1:
            return -1
        if n == 1:
            return 1
        
        judge = trust[0][1]
        people = set()
        for p, j in trust:
            if judge != j:
                return -1
            people.add(p)

        return judge if len(people) == n - 1 else -1