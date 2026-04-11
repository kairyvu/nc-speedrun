class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        visited = set()
        l = 0
        for r in range(len(nums)):
            if nums[r] in visited:
                return True
            visited.add(nums[r])

            if r - l == k:
                visited.remove(nums[l])
                l += 1
        return False