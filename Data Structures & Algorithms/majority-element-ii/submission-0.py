class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num1, num2 = [-1, 0], [-1, 0]
        n = len(nums)

        for num in nums:
            if num1[0] == num:
                num1[1] += 1
            elif num2[0] == num:
                num2[1] += 1
            elif num1[1] == 0:
                num1 = [num, 1]
            elif num2[1] == 0:
                num2 = [num, 1]
            else:
                num1[1] -= 1
                num2[1] -= 1
        
        res = []
        count1, count2 = 0, 0
        for num in nums:
            if num == num1[0]:
                count1 += 1
            elif num == num2[0]:
                count2 += 1
        if count1 > n // 3:
            res.append(num1[0])
        if count2 > n // 3:
            res.append(num2[0])
        
        return res