class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol, res = [], []
        visited = set()
        self._dfs(nums, 0, visited, sol, res)
        return res
    
    def _dfs(self, nums, idx, visited, sol, res):
        if len(sol) == len(nums):
            res.append(sol[:])
            return
        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                sol.append(nums[i])
                self._dfs(nums, i+1, visited, sol, res)
                sol.pop()
                visited.remove(i)