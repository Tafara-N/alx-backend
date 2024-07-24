#!/usr/bin/env python3

"""
A class LFUCache that inherits from BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    A class LFUCache that inherits from BaseCaching

    Function implements the Least Frequently Used (LFU)
        caching algorithm
    """

    def __init__(self):
        """
        Instantiate LFUCache
        """

        super().__init__()
        self.lfu = {}
        self.queue = []

    def put(self, key, item):
        """
        Add key: value pair to cache data
        """

        if key and item:
            if (
                len(self.queue) >= self.MAX_ITEMS
                and not self.cache_data.get(key)
            ):

            deleted_key = self.queue.pop(0)
            self.lfu.pop(deleted_key)
            self.cache_data.pop(deleted_key)
            print(f"DISCARD: {deleted_key}")

        if self.cache_data.get(key):
            self.queue.remove(key)
            self.lfu[key] += 1
        else:
            self.lfu[key] = 0

        inserted_index = 0

        while (
            inserted_index < len(self.queue)
            and not self.lfu[self.queue[inserted_index]]
        ):
            inserted_index += 1
        self.queue.insert(inserted_index, key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Get value given key from cache data
        """

        self.lfu[key] += 1
        index = self.queue.index(key)

        if index + 1 < len(self.queue):
            next_key = self.queue[index + 1]

            while self.lfu[key] >= self.lfu[next_key]:
                (self.queue[index], self.queue[index + 1]) = \
                    (self.queue[index + 1], self.queue[index])

                index += 1
                if index + 1 < len(self.queue):
                    next_key = self.queue[index + 1]
                else:

        return self.cache_data[key] if key in self.cache_data else None
