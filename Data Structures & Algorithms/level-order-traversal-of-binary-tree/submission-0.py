# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = deque([root, None])
        res, lvl = [], []
        while queue:
            curr = queue.popleft()
            if curr:
                lvl.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            else:
                if queue:
                    queue.append(None)
                res.append(lvl[:])
                lvl = []
        return res