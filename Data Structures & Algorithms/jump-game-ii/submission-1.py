class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        left = right = 0
        while right < len(nums) - 1:
            max_pos = 0
            for i in range(left, right + 1):
                max_pos = max(max_pos, i + nums[i])
            left = right + 1
            right = max_pos
            res += 1
        return res