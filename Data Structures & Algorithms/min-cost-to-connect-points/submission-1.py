import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj_list = [[] for _ in range(len(points))]
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj_list[i].append((j, dist))
                adj_list[j].append((i, dist))

        res = 0
        visited = set()
        min_heap = [(0, 0)]
        while len(visited) < len(points):
            cost, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            res += cost
            visited.add(node)
            for nei, dist in adj_list[node]:
                if nei not in visited:
                    heapq.heappush(min_heap, (dist, nei))
        return res