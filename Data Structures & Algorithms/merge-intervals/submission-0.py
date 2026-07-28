class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        res = []
        for i in intervals:
            if len(res) == 0 or i[0] > res[-1][1]:
                res.append(i)
            else:
                res[-1][1] = max(res[-1][1], i[1])
        return res