class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, max(piles)
        while start + 1 < end:
            mid = (start + end) // 2
            if self._can_finish(piles, h, mid):
                end = mid
            else:
                start = mid
        if self._can_finish(piles, h, start):
            return start
        return end

    def _can_finish(self, piles, h, target):
        total = sum(math.ceil(p / target) for p in piles)
        return total <= h