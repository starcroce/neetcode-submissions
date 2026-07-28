"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map = {None: None}
        curr = head
        while curr:
            if curr not in node_map:
                node_map[curr] = Node(curr.val)
            if curr.next and curr.next not in node_map:
                node_map[curr.next] = Node(curr.next.val)
            if curr.random and curr.random not in node_map:
                node_map[curr.random] = Node(curr.random.val)
            node_map[curr].next = node_map[curr.next]
            node_map[curr].random = node_map[curr.random]
            curr = curr.next
        return node_map[head]