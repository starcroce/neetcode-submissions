class TrieNode:
    def __init__(self):
        self.chars = {}
        self.word = ""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = self._build_trie(words)
        visited, res = set(), set()
        row, col = len(board), len(board[0])
        for i in range(row):
            for j in range(col):
                self._find_dfs(board, root, visited, i, j, res)
        return list(res)

    def _build_trie(self, words):
        root = TrieNode()
        for w in words:
            curr = root
            for c in w:
                if c not in curr.chars:
                    curr.chars[c] = TrieNode()
                curr = curr.chars[c]
            curr.word = w
        return root

    def _find_dfs(self, board, node, visited, r, c, res):
        row, col = len(board), len(board[0])
        if r < 0 or r >= row or c < 0 or c >= col:
            return
        if (r, c) in visited or board[r][c] not in node.chars:
            return
        visited.add((r, c))
        node = node.chars[board[r][c]]
        if node.word:
            res.add(node.word)
        self._find_dfs(board, node, visited, r+1, c, res)
        self._find_dfs(board, node, visited, r-1, c, res)
        self._find_dfs(board, node, visited, r, c+1, res)
        self._find_dfs(board, node, visited, r, c-1, res)
        visited.remove((r, c))