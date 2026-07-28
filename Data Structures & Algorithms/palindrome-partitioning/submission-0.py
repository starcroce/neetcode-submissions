class Solution:
    def partition(self, s: str) -> List[List[str]]:
        sol, res = [], []
        self._dfs(s, 0, sol, res)
        return res

    def _dfs(self, s, pos, sol, res):
        if pos == len(s):
            res.append(sol[:])
            return
        for i in range(pos, len(s)):
            if self._is_palindrome(s, pos, i):
                sol.append(s[pos:i+1])
                self._dfs(s, i+1, sol, res)
                sol.pop()

    def _is_palindrome(self, s, start, end):
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True