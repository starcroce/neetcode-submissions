"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from collections import defaultdict

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        time_to_room = defaultdict(int)
        for i in intervals:
            time_to_room[i.start] += 1
            time_to_room[i.end] -= 1
        curr, res = 0, 0
        for i in sorted(time_to_room.keys()):
            curr += time_to_room[i]
            res = max(res, curr)
        return res