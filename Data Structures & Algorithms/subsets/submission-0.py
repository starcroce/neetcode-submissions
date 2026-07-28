class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        self._dfs(nums, 0, sol, res)
        return res

    def _dfs(self, nums, idx, sol, res):
        res.append(sol[:])
        for i in range(idx, len(nums)):
            sol.append(nums[i])
            self._dfs(nums, i+1, sol, res)
            sol.pop()