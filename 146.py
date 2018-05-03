class LRUCache:
    class _QueueNode:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.next = None

    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = LRUCache._QueueNode(None, None)
        self.queue_tail = self.queue
        self.pre_node = {}

    def move_to_tail(self, pre_node):
        node = pre_node.next

        self.pre_node[node.next.key] = pre_node
        pre_node.next = node.next

        self.pre_node[node.key] = self.queue_tail
        self.queue_tail.next = node
        self.queue_tail = node

        node.next = None

    def remove_head(self):
        node = self.queue.next

        self.pre_node[node.next.key] = self.queue
        self.queue.next = node.next
        self.pre_node.pop(node.key)

    def get(self, key):
        if self.queue_tail.key == key:
            return self.queue_tail.val
        pre_node = self.pre_node.get(key, None)
        if pre_node:
            res = pre_node.next.val
            self.move_to_tail(pre_node)
            return res
        return -1

    def put(self, key, value):
        if self.queue_tail.key == key:
            self.queue_tail.val = value
            return
        if key in self.pre_node:
            pre_node = self.pre_node[key]
            pre_node.next.val = value
            self.move_to_tail(pre_node)
        else:
            node = LRUCache._QueueNode(key, value)
            self.pre_node[key] = self.queue_tail
            self.queue_tail.next = node
            self.queue_tail = node
            if len(self.pre_node) > self.capacity:
                self.remove_head()


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))
