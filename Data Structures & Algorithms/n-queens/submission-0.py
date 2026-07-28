class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        res = []
        col_set, diag_set_1, diag_set_2 = set(), set(), set()
        self._dfs(n, board, 0, col_set, diag_set_1, diag_set_2, res)
        return res

    def _dfs(self, n, board, r, col_set, diag_set_1, diag_set_2, res):
        if r == n:
            res.append(["".join(row) for row in board])
            return
        for c in range(n):
            if c in col_set or r + c in diag_set_1 or r - c in diag_set_2:
                continue
            col_set.add(c)
            diag_set_1.add(r + c)
            diag_set_2.add(r - c)
            board[r][c] = "Q"
            self._dfs(n, board, r + 1, col_set, diag_set_1, diag_set_2, res)
            board[r][c] = "."
            diag_set_2.remove(r - c)
            diag_set_1.remove(r + c)
            col_set.remove(c)
