# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_depth = self._max_depth(root.left)
        right_depth = self._max_depth(root.right)
        diameter = left_depth + right_depth
        child_dia = max(
            self.diameterOfBinaryTree(root.left),
            self.diameterOfBinaryTree(root.right)
        )
        return max(diameter, child_dia)
        
    def _max_depth(self, node):
        if node is None:
            return 0
        return max(
            self._max_depth(node.left),
            self._max_depth(node.right)
        ) + 1