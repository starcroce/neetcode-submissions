import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            if second > first:
                heapq.heappush(heap, first - second)

        if len(heap) == 1:
            return -heap[0]
        else:
            return 0