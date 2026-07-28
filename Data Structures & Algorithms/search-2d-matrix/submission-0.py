class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        nums_col = [matrix[i][0] for i in range(row)]
        idx_row = self._binary_search(nums_col, target)
        if idx_row == -1:
            return False
        idx_col = self._binary_search(matrix[idx_row], target)
        if idx_col == -1:
            return False
        return matrix[idx_row][idx_col] == target

    def _binary_search(self, nums, target):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid
        if nums[end] <= target:
            return end
        elif nums[start] <= target:
            return start
        else:
            return -1