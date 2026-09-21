class LRUNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_map = {}
        self.head = LRUNode(-1, -1)
        self.tail = LRUNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1
        node = self.node_map[key]
        self._remove(node)
        self._add_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = LRUNode(key, value)
        self._add_to_head(node)
        if key in self.node_map:
            self._remove(self.node_map[key])
        self.node_map[key] = node

        if len(self.node_map) > self.capacity:
            temp = self.tail.prev
            self._remove(temp)
            del self.node_map[temp.key]

    def _remove(self, node):
        temp_prev = node.prev
        temp_next = node.next
        temp_prev.next = temp_next
        temp_next.prev = temp_prev

    def _add_to_head(self, node):
        temp = self.head.next
        self.head.next = node
        node.next = temp
        temp.prev = node
        node.prev = self.head
        
