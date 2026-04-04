"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        meetingTime = {}
        for i in range(len(intervals)):
            start, end = intervals[i].start, intervals[i].end
            meetingTime[start] = meetingTime.get(start, 0) + 1
            meetingTime[end] = meetingTime.get(end, 0) - 1
        
        currRoom = maxRoom = 0
        for t in sorted(meetingTime):
            currRoom += meetingTime[t]
            maxRoom = max(maxRoom, currRoom)
        return maxRoom