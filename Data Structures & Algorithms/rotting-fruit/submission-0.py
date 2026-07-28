from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        queue = deque([])
        fresh = 0
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1

        res = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue and fresh:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for di, dj in directions:
                    ii, jj = i + di, j + dj
                    if ii < 0 or ii >= row or jj < 0 or jj >= col:
                        continue
                    if grid[ii][jj] == 1:
                        grid[ii][jj] = 2
                        fresh -= 1
                        queue.append((ii, jj))
            res += 1

        return res if fresh == 0 else -1