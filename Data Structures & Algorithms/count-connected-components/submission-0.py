from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        visited = set()

        res = 0
        for i in range(n):
            if i not in visited:
                queue = deque([i])
                while queue:
                    curr = queue.popleft()
                    visited.add(curr)
                    for nei in adj_list[curr]:
                        if nei not in visited:
                            queue.append(nei)
                res += 1

        return res
