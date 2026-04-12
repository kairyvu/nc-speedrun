class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        used = [False] * n
        nums.sort(reverse=True)

        def backtrack(i, currSum, k):
            if k == 0:
                return True
            if currSum == target:
                return backtrack(0, 0, k - 1)

            for j in range(i, n):
                if used[j] or currSum + nums[j] > target or (j > i and nums[j] == nums[j - 1] and not used[j - 1]):
                    continue
                used[j] = True
                if backtrack(j + 1, currSum + nums[j], k):
                    return True
                used[j] = False
                if currSum == 0:
                    return False
            return False
        
        return backtrack(0, 0, k)
                