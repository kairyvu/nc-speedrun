class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        curr = []

        def backtrack(i, target):
            if target == 0:
                res.append(curr.copy())
                return
            
            for j in range(i, len(candidates)):
                if target - candidates[j] < 0:
                    return
                if j > i and candidates[j - 1] == candidates[j]:
                    continue
                curr.append(candidates[j])
                backtrack(j + 1, target - candidates[j])
                curr.pop()
        
        backtrack(0, target)
        return res