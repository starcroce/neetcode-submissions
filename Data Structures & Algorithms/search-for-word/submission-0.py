class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited, curr = set(), []
        row, col = len(board), len(board[0])
        for i in range(row):
            for j in range(col):
                if self._search_dfs(board, word, i, j, 0, visited):
                    return True
        return False

    def _search_dfs(self, board, word, i, j, idx, visited):
        row, col = len(board), len(board[0])
        if i < 0 or i >= row or j < 0 or j >= col:
            return False
        if (i, j) in visited:
            return False
        if board[i][j] != word[idx]:
            return False
        if idx == len(word) - 1:
            return True
        visited.add((i, j))
        found = (
            self._search_dfs(board, word, i+1, j, idx+1, visited)
            or self._search_dfs(board, word, i-1, j, idx+1, visited)
            or self._search_dfs(board, word, i, j+1, idx+1, visited)
            or self._search_dfs(board, word, i, j-1, idx+1, visited)
        )
        visited.remove((i, j))
        return found
