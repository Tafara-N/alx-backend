#!/usr/bin/python3

"""
A class `LIFOCache` that inherits from `BaseCaching` and is a caching system
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    A class `LIFOCache` that inherits from `BaseCaching`
    """

    def __init__(self):
        """
        Instantiate `LIFOCache`
        """
        
        super().__init__()
        self.cache_data = []

    def put(self, key, item):
        """
        Add key/value pair to cache data
        """

        if key and item:
            if key in self.cache_data:
                self.cache_data.remove(key)
            self.cache_data.append(key)
            self.cache_data.append(item)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                del_key = self.cache_data.pop(0)
                del self.cache_data[del_key]
                print(f"DISCARD: {del_key}")

    def get(self, key):
        """
        Get value given key from cache data
        """

        if key in self.cache_data:
            return self.cache_data[key]
        return None
