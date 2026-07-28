class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sol, res = [], []
        self._dfs(nums, target, 0, sol, res)
        return res
        
    def _dfs(self, nums, target, idx, sol, res):
        if sum(sol) == target:
            res.append(sol[:])
            return
        if sum(sol) > target:
            return
        for i in range(idx, len(nums)):
            sol.append(nums[i])
            self._dfs(nums, target, i, sol, res)
            sol.pop()