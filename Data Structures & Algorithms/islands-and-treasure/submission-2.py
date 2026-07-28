from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])
        queue = deque([])
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    queue.append((i, j))
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for di, dj in directions:
                    ii, jj = i + di, j + dj
                    if ii < 0 or ii >= row or jj < 0 or jj >= col:
                        continue
                    if grid[ii][jj] != 2147483647:
                        continue
                    grid[ii][jj] = grid[i][j] + 1
                    queue.append((ii, jj))
