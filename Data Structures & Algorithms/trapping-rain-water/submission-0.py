class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        max_pos, max_height = 0, height[0]
        for i in range(1, len(height)):
            if height[i] > max_height:
                max_pos = i
                max_height = height[i]
        res = 0
        left_max = height[0]
        for i in range(1, max_pos):
            if height[i] >= left_max:
                left_max = height[i]
            else:
                res += min(max_height, left_max) - height[i]
        right_max = height[-1]
        for i in range(len(height)-2, max_pos, -1):
            if height[i] >= right_max:
                right_max = height[i]
            else:
                res += min(max_height, right_max) - height[i]
        return res