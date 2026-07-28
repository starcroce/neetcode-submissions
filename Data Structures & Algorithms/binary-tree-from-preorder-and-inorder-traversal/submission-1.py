# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        l = len(preorder)
        idx_map = {v: i for i, v in enumerate(inorder)}
        return self._build_tree(preorder, 0, l-1, inorder, 0, l-1, idx_map)

    def _build_tree(self, preorder, pstart, pend, inorder, istart, iend, idx_map):
        if iend - istart < 0 or iend - istart != pend - pstart:
            return None
        root = TreeNode(preorder[pstart])
        root_idx = idx_map[root.val]
        left_node_cnt = root_idx - istart
        root.left = self._build_tree(
            preorder, pstart + 1, pstart + left_node_cnt,
            inorder, istart, root_idx - 1,
            idx_map,
        )
        root.right = self._build_tree(
            preorder, pstart + left_node_cnt + 1, pend,
            inorder, root_idx + 1, iend,
            idx_map,
        )
        return root