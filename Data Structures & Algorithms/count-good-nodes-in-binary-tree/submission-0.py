# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return self._dfs(root, root.val)

    def _dfs(self, node, curr_max):
        if node is None:
            return 0
        if node.val >= curr_max:
            return self._dfs(node.left, node.val) + self._dfs(node.right, node.val) + 1
        else:
            return self._dfs(node.left, curr_max) + self._dfs(node.right, curr_max)
        