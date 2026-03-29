class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        i + 1
        i + 2
        i = 5
        len(cost) = 5 0->4
        block 3 jumps 2
        block 4 jumps 1
        sumCost = []
        newCost = min(cost[3] + sumCost[3], cost[4] + sumCost[4])

        Time: O(n)
        Space: O(1)
        '''

        cost1, cost2 = 0, 0

        for i in range(2, len(cost) + 1):
            temp = min(cost[i - 2] + cost1, cost[i - 1] + cost2) 
            cost1 = cost2
            cost2 = temp
        return cost2