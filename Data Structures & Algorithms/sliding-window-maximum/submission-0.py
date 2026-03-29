class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque() # decreasing
        for i in range(k - 1):
            while dq and dq[-1][0] <= nums[i]:
                dq.pop()
            dq.append((nums[i], i))
        
        res = []
        for i in range(k - 1, len(nums)):
            while dq and dq[-1][0] <= nums[i]:
                dq.pop()
            dq.append((nums[i], i))
            while dq and dq[0][1] < i - k + 1:
                dq.popleft()
            res.append(dq[0][0])
        return res