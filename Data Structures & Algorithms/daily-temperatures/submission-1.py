class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        nextWarmer = [0] * n
        monoStack = [] # decreasing (temp, index)

        for i in range(len(temperatures) - 1, -1, -1):
            while monoStack and monoStack[-1][0] <= temperatures[i]:
                monoStack.pop()            
            index = i if not monoStack else monoStack[-1][1]
            nextWarmer[i] = index - i
            monoStack.append((temperatures[i], i))
        return nextWarmer

        # [30,38,30,36,35,40,28]
        # i = 4
        # temp = 35
        # monoStack = (40, 5) (35, 4)
        # nextWarmer = [0,0,0,0,0,0,0]