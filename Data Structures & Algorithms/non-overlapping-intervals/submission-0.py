class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda i : i[1])
        curr_end = intervals[0][1]
        res = 0
        for i in range(1, len(intervals)):
            if curr_end > intervals[i][0]:
                res += 1
            else:
                curr_end = intervals[i][1]
        return res
