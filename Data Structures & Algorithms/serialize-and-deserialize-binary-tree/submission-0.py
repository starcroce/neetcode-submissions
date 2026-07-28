# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        self._visit_node(root, res)
        return " ".join(res)

    def _visit_node(self, node, res):
        if node is None:
            res.append("#")
        else:
            res.append(str(node.val))
            self._visit_node(node.left, res)
            self._visit_node(node.right, res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = deque(data.split(" "))
        return self._visit_val(vals)

    def _visit_val(self, vals):
        curr = vals.popleft()
        if curr == "#":
            return None
        node = TreeNode(int(curr))
        node.left = self._visit_val(vals)
        node.right = self._visit_val(vals)
        return node