class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        nums_to_chars = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        sol, res = [], []
        self._dfs(digits, nums_to_chars, 0, sol, res)
        return res

    def _dfs(self, digits, nums_to_chars, pos, sol, res):
        if len(sol) == len(digits):
            res.append("".join(sol))
            return
        for c in nums_to_chars[digits[pos]]:
            sol.append(c)
            self._dfs(digits, nums_to_chars, pos + 1, sol, res)
            sol.pop()