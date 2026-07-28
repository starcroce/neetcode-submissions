from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])
        queue = deque([])
        visited = set()
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    queue.append((i, j))
        
        dist = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if i < 0 or i >= row or j < 0 or j >= col:
                    continue
                if (i, j) in visited or grid[i][j] == -1:
                    continue
                grid[i][j] = dist
                visited.add((i, j))
                queue.append((i + 1, j))
                queue.append((i - 1, j))
                queue.append((i, j + 1))
                queue.append((i, j - 1))
            dist += 1