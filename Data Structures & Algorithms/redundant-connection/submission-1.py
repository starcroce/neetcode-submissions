from collections import deque

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        indegrees = [0 for _ in range(n + 1)]
        adj_list = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
            indegrees[u] += 1
            indegrees[v] += 1

        q = deque([])
        for i in range(1, n + 1):
            if indegrees[i] == 1:
                q.append(i)

        while q:
            node = q.popleft()
            if indegrees[node] == 0:
                continue
            indegrees[node] = 0
            for nei in adj_list[node]:
                indegrees[nei] -= 1
                if indegrees[nei] == 1:
                    q.append(nei)

        for u, v in reversed(edges):
            if indegrees[u] > 1 and indegrees[v] > 1:
                return [u, v]
        return []