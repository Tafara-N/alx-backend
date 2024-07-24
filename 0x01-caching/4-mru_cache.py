#!/usr/bin/env python3

"""
A class `MRUCache` that inherits from BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    A class `MRUCache` that inherits from `BaseCaching`
    """

    def __init__(self):
        """
        Instantiate `MRUCache`
        """

        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        Add key: value pair to cache data
        """

        if key and item:
            if self.cache_data.get(key):
                self.queue.remove(key)
            self.queue.append(key)
            self.cache_data[key] = item

            if len(self.queue) > self.MAX_ITEMS:
                deleted_key = self.queue.pop(-2)
                self.cache_data.pop(deleted_key)
                print(f"DISCARD: {deleted_key}")

    def get(self, key):
        """
        Get value given key from cache data
        """

        if key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data[key]
        return None
