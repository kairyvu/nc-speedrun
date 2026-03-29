class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        res = 0

        while l < r:
            if height[l] <= height[r]:
                maxL = max(maxL, height[l])
                res += maxL - height[l]
                l += 1
            else:
                maxR = max(maxR, height[r])
                res += maxR - height[r]
                r -= 1
        return res