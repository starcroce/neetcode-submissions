from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        visited = set()
        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i, j) not in visited:
                    self._expand(grid, i, j, visited)
                    res += 1
        return res

    def _expand(self, grid, i, j, visited):
        row, col = len(grid), len(grid[0])
        queue = deque([(i, j)])
        while len(queue):
            r, c = queue.popleft()
            if r < 0 or r >= row or c < 0 or c >= col:
                continue
            if grid[r][c] == "0" or (r, c) in visited:
                continue
            visited.add((r, c))
            queue.append((r-1, c))
            queue.append((r+1, c))
            queue.append((r, c-1))
            queue.append((r, c+1))