class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sol, res = [], []
        candidates.sort()
        self._dfs(candidates, target, 0, sol, res)
        return res

    def _dfs(self, candidates, target, idx, sol, res):
        if sum(sol) == target:
            res.append(sol[:])
            return
        if sum(sol) > target:
            return
        for i in range(idx, len(candidates)):
            if i > idx and candidates[i] == candidates[i-1]:
                continue
            sol.append(candidates[i])
            self._dfs(candidates, target, i+1, sol, res)
            sol.pop()