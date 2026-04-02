class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[n - 1] == "1":
            return False       
        q, farthest = deque([0]), 0

        while q:
            index = q.popleft()
            start = max(farthest + 1, index + minJump)
            if index + maxJump >= n - 1 and index + minJump <= n - 1:
                return True

            for j in range(start, min(index + maxJump + 1, n)):
                if s[j] == "0":
                    q.append(j)
            farthest = index + maxJump
        
        return False