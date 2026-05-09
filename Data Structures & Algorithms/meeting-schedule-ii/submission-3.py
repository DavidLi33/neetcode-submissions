"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start, end = [], []
        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        
        start.sort()
        end.sort()
        res, count = 0, 0
        s_index, e_index = 0, 0
        while s_index < len(intervals):
            if start[s_index] < end[e_index]:
                s_index += 1
                count += 1
            else:
                e_index += 1
                count -= 1
            res = max(res, count)
        return res