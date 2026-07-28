"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda i: i.start)
        for i in range(1, len(sorted_intervals)):
            i1 = sorted_intervals[i-1]
            i2 = sorted_intervals[i]
            if i1.end > i2.start:
                return False
        return True