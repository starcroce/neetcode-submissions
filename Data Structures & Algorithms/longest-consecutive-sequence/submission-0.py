class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0
        for n in nums:
            if n - 1 not in num_set:
                curr_n, curr_len = n + 1, 1
                while curr_n in num_set:
                    curr_len += 1
                    curr_n += 1
                res = max(res, curr_len)
        return res