class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self._is_valid_numbers(row):
                return False

        row, col = len(board), len(board[0])
        for j in range(col):
            curr_col = [board[i][j] for i in range(row)]
            if not self._is_valid_numbers(curr_col):
                return False

        for r in range(3):
            for c in range(3):
                box = []
                for i in range(r*3, r*3+3):
                    for j in range(c*3, c*3+3):
                        box.append(board[i][j])
                if not self._is_valid_numbers(box):
                    return False

        return True

    def _is_valid_numbers(self, nums):
        visited = [False for _ in range(10)]
        for n in nums:
            if n == ".":
                continue
            if visited[int(n)]:
                return False
            visited[int(n)] = True
        return True