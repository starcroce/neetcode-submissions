class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid
                else:
                    end = mid
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            return -1