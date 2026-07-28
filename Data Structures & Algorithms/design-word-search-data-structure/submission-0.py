class TrieNode:

    def __init__(self):
        self.child_map = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.child_map:
                curr.child_map[c] = TrieNode()
            curr = curr.child_map[c]
        curr.is_word = True

    def search(self, word: str) -> bool:
        return self._dfs(word, 0, self.root)

    def _dfs(self, word, idx, node):
        if idx == len(word):
            return node.is_word
        curr_char = word[idx]
        if curr_char != ".":
            if curr_char not in node.child_map:
                return False
            else:
                return self._dfs(word, idx+1, node.child_map[curr_char])
        else:
            return any([
                self._dfs(word, idx+1, node.child_map[c])
                for c in node.child_map
            ])