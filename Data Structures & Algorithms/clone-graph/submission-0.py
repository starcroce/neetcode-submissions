"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        node_map = {node: Node(node.val)}
        queue = deque([node])
        while len(queue):
            curr = queue.popleft()
            for n in curr.neighbors:
                if n not in node_map:
                    node_map[n] = Node(n.val)
                    queue.append(n)
                mirror_node = node_map[curr]
                mirror_node.neighbors.append(node_map[n])
        return node_map[node]