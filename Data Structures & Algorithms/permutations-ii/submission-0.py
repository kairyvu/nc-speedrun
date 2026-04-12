class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        res = []
        perm = []
        n = len(nums)

        def backtrack():
            if len(perm) == n:
                res.append(perm.copy())
                return
            
            for num in counter:
                if counter[num] == 0:
                    continue
                
                perm.append(num)
                counter[num] -= 1
                backtrack()
                perm.pop()
                counter[num] += 1
        
        backtrack()
        return res