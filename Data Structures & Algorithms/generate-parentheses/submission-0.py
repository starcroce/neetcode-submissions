class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sol, res = [], []
        self._dfs(n, n, sol, res)
        return res

    def _dfs(self, left, right, sol, res):
        if left == 0 and right == 0:
            res.append("".join(sol))
            return
        if left > 0:
            sol.append("(")
            self._dfs(left-1, right, sol, res)
            sol.pop()
        if left < right:
            sol.append(")")
            self._dfs(left, right-1, sol, res)
            sol.pop()