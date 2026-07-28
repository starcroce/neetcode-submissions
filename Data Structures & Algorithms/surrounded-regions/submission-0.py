from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row, col = len(board), len(board[0])
        queue = deque([])
        for i in range(row):
            if board[i][0] == "O":
                queue.append((i, 0))
            if board[i][col-1] == "O":
                queue.append((i, col-1))
        for j in range(col):
            if board[0][j] == "O":
                queue.append((0, j))
            if board[row-1][j] == "O":
                queue.append((row-1, j))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            i, j = queue.popleft()
            if board[i][j] == "O":
                board[i][j] = "#"
                for di, dj in directions:
                    ii, jj = i + di, j + dj
                    if 0 <= ii < row and 0 <= jj < col:
                        queue.append((ii, jj))

        for i in range(row):
            for j in range(col):
                if board[i][j] == "#":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"