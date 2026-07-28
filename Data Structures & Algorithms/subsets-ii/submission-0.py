class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        sol, res = [], []
        self._dfs(nums, 0, sol, res)
        return res

    def _dfs(self, nums, idx, sol, res):
        res.append(sol[:])
        for i in range(idx, len(nums)):
            if i == idx or nums[i] != nums[i-1]:
                sol.append(nums[i])
                self._dfs(nums, i+1, sol, res)
                sol.pop()
