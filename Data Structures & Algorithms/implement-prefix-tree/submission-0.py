class PrefixTreeNode:
    
    def __init__(self):
        self.child_map = {}
        self.is_end = False

class PrefixTree:

    def __init__(self):
        self.root = PrefixTreeNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.child_map:
                curr.child_map[c] = PrefixTreeNode()
            curr = curr.child_map[c]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.child_map:
                return False
            curr = curr.child_map[c]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.child_map:
                return False
            curr = curr.child_map[c]
        return True
        