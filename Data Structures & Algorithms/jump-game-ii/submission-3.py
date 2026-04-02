class Solution:
    def jump(self, nums: List[int]) -> int:
        # if len(nums) < 2:
        #     return 0
        count = 0
        index, farthest = 0, 0

        while farthest < len(nums) - 1:
            currReach = farthest
            for i in range(index, farthest + 1):
                currReach = max(currReach, nums[i] + i)
            index = farthest + 1
            farthest = currReach
            count += 1
        
        return count