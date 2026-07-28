# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        self._dfs(root, res)
        return res[k-1]

    def _dfs(self, node, res):
        if node is None:
            return
        self._dfs(node.left, res)
        res.append(node.val)
        self._dfs(node.right, res)