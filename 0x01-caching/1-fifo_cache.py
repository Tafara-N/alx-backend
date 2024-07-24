#!/usr/bin/python3

"""
A class `FIFOCache` that inherits from `BaseCaching` and is a caching system
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    A class `FIFOCache` that inherits from `BaseCaching`
    """

    def __init__(self):
        """
        Instantiate `FIFOCache`
        """

        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Assign to the dictionary `cache_data` the item value for the key `key`
        """

        if key is None or item is None:
            return

        if (len(self.cache_data) >= BaseCaching.MAX_ITEMS and
                key not in self.cache_data):

            discarded = self.keys.pop(0)
            del self.cache_data[discarded]
            print("DISCARD:", discarded)

        self.cache_data[key] = item
        self.keys.append(key)

    def get(self, key):
        """
        Return the value in `cache_data` linked to `key` key
        """

        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
