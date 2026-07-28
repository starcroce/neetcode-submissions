class LRUCacheNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_map = {}
        self.head = LRUCacheNode(-1, -1)
        self.tail = LRUCacheNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1
        new_node = self.node_map[key]
        self._remove_node(new_node)
        self._add_node(new_node)
        return new_node.val

    def put(self, key: int, value: int) -> None:
        new_node = LRUCacheNode(key, value)
        self._add_node(new_node)
        if key in self.node_map:
            self._remove_node(self.node_map[key])
        self.node_map[key] = new_node
        if len(self.node_map) > self.capacity:
            temp = self.tail.prev
            self._remove_node(temp)
            del self.node_map[temp.key]

    def _remove_node(self, node):
        temp_p = node.prev
        temp_n = node.next
        temp_p.next = temp_n
        temp_n.prev = temp_p

    def _add_node(self, node):
        temp = self.head.next
        self.head.next = node
        node.next = temp
        temp.prev = node
        node.prev = self.head

        
