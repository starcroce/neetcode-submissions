import heapq

class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.large, num)
        large_top = heapq.heappop(self.large)
        heapq.heappush(self.small, -large_top)
        if len(self.small) > len(self.large):
            heapq.heappush(
                self.large,
                -heapq.heappop(self.small),
            )

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        else:
            return self.large[0]
        