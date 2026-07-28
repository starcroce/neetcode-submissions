from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        pac = [[False for _ in range(col)] for _ in range(row)]
        atl = [[False for _ in range(col)] for _ in range(row)]

        src_pac, src_atl = [], []
        for i in range(row):
            src_pac.append((i, 0))
            src_atl.append((i, col - 1))
        for j in range(col):
            src_pac.append((0, j))
            src_atl.append((row - 1, j))

        self._bfs(heights, src_pac, pac)
        self._bfs(heights, src_atl, atl)

        res = []
        for i in range(row):
            for j in range(col):
                if pac[i][j] and atl[i][j]:
                    res.append([i, j])
        return res

    def _bfs(self, heights, source, ocean):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        row, col = len(heights), len(heights[0])
        queue = deque(source)
        while queue:
            i, j = queue.popleft()
            ocean[i][j] = True
            for di, dj in directions:
                ii, jj = i + di, j + dj
                if ii < 0 or ii >= row or jj < 0 or jj >= col:
                    continue
                if ocean[ii][jj] is False and heights[ii][jj] >= heights[i][j]:
                    queue.append((ii, jj))