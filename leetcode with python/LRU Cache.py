# -*- coding:utf-8 -*-
class LRUCache:
    class LRUNode:
        def __init__(self, key, value):
            self.prev = None
            self.next = None
            self.key = key
            self.value = value

    # @param capacity, an integer
    def __init__(self, capacity):
        self.map = {}
        self.list_head = LRUCache.LRUNode(-1, -1)
        self.list_tail = LRUCache.LRUNode(-1, -1)
        self.list_head.next = self.list_tail
        self.list_tail.prev = self.list_head
        self.capacity = capacity

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def append_node(self, new_node):
        last_node = self.list_tail.prev
        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self.list_tail
        self.list_tail.prev = new_node

    # @return an integer
    def get(self, key):
        if self.map.has_key(key):
            cur = self.map.get(key)
            self.remove_node(cur)
            self.append_node(cur)
            return cur.value
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if self.map.has_key(key):
            old_node = self.map.get(key)
            self.remove_node(old_node)
            old_node.value = value
            self.append_node(old_node)
        else:
            if len(self.map) >= self.capacity:
                del_node = self.list_head.next
                self.remove_node(del_node)
                del self.map[del_node.key]
            new_node = LRUCache.LRUNode(key, value)
            self.append_node(new_node)
            self.map[key] = new_node
