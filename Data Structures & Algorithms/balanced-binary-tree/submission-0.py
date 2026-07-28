# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        left_height = self._get_height(root.left)
        right_height = self._get_height(root.right)
        
        if abs(left_height - right_height) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def _get_height(self, node):
        if node is None:
            return 0
        return max(
            self._get_height(node.left),
            self._get_height(node.right),
        ) + 1
