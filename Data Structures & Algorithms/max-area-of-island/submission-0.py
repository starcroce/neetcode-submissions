from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        visited = set()
        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (i, j) not in visited:
                    curr = self._bfs(grid, i, j, visited)
                    res = max(res, curr)
        return res

    def _bfs(self, grid, i, j, visited):
        row, col = len(grid), len(grid[0])
        queue = deque([(i, j)])
        curr = 0
        while len(queue):
            r, c = queue.popleft()
            if r < 0 or r >= row or c < 0 or c >= col:
                continue
            if grid[r][c] == 0 or (r, c) in visited:
                continue
            visited.add((r, c))
            curr += 1
            queue.append((r-1, c))
            queue.append((r+1, c))
            queue.append((r, c-1))
            queue.append((r, c+1))
        return curr