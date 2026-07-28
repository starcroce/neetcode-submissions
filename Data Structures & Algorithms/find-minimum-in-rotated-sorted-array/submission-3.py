class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        target = nums[-1]
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > target:
                start = mid
            else:
                end = mid
        return min(nums[start], nums[end])