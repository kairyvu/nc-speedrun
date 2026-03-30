class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []

        for i in range(len(intervals)):
            if not res:
                res.append(intervals[i])
            elif res[-1][1] >= intervals[i][0]:
                start, end = res.pop()
                newInterval = [min(start, intervals[i][0]), max(end, intervals[i][1])]
                res.append(newInterval)
            else:
                res.append(intervals[i])
        return res