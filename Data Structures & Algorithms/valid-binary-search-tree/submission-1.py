# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self._dfs(root, float("-inf"), float("inf"))

    def _dfs(self, node, low, high):
        if node is None:
            return True
        if node.val <= low or node.val >= high:
            return False
        return self._dfs(node.left, low, node.val) and self._dfs(node.right, node.val, high)