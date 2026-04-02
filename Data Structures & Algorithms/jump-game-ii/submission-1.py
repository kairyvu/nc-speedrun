class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        count = 1
        index, maxIndex = 0, nums[0]

        while maxIndex < len(nums) - 1:
            currMaxIndex = maxIndex
            while index <= maxIndex:
                currMaxIndex = max(currMaxIndex, index + nums[index])
                index += 1
            
            maxIndex = currMaxIndex
            count += 1
        
        return count