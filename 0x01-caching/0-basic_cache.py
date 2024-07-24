#!/usr/bin/python3

"""
A class `BasicCache` that inherits from `BaseCaching` and is a caching system
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    A class `BasicCache` that inherits from `BaseCaching`
    """

    def __init__(self):
        """
        Instantiate `BasicCache`
        """
        super().__init__()

    def put(self, key, item):
        """
        Assign to the dictionary `cache_data` the item value for the key `key`
        """

        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Return the value in `cache_data` linked to `key` key
        """

        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
