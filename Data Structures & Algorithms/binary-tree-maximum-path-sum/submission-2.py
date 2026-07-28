# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return self._get_max_path_sum(root)[0]

    def _get_max_path_sum(self, node):
        if node is None:
            return float("-inf"), float("-inf")
        left_max, left_max_single = self._get_max_path_sum(node.left)
        right_max, right_max_single = self._get_max_path_sum(node.right)
        curr_max = max(
            left_max, right_max, node.val,
            left_max_single + node.val,
            right_max_single + node.val,
            left_max_single + node.val + right_max_single,
        )
        curr_max_single = max(
            node.val,
            left_max_single + node.val,
            right_max_single + node.val,
        )
        return curr_max, curr_max_single