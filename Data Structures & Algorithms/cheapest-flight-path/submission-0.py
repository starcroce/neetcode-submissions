from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf") for _ in range(n)]
        prices[src] = 0
        adj_list = [[] for _ in range(n)]
        for u, v, c in flights:
            adj_list[u].append((v, c))

        queue = deque([(0, src, 0)])
        while queue:
            cost, node, stops = queue.popleft()
            if stops > k:
                continue
            for nei, c in adj_list[node]:
                new_cost = cost + c
                if new_cost < prices[nei]:
                    prices[nei] = new_cost
                    queue.append((new_cost, nei, stops + 1))

        if prices[dst] == float("inf"):
            return -1
        return prices[dst]
