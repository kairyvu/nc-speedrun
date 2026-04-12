class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        edge = total // 4
        matchsticks.sort(reverse=True)

        def backtrack(i, square):
            if i == len(matchsticks):
                return len(set(square)) == 1 and square[0] == edge

            for j in range(4):
                if j > 0 and square[j - 1] == square[j]:
                    continue
                if square[j] + matchsticks[i] <= edge:
                    square[j] += matchsticks[i]
                    if backtrack(i + 1, square):
                        return True
                    square[j] -= matchsticks[i]
            return False
        
        return backtrack(0, [0, 0, 0, 0])
