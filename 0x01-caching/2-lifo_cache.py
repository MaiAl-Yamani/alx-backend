#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A class LIFOCache that inherits from
    BaseCaching and is a caching system:"""
    lastkey = None

    def __init__(self):
        """ init function"""
        super().__init__()

    def put(self, key, item):
        """add items to dict"""
        if key is not None and item is not None:
            if len(self.cache_data) == self.MAX_ITEMS and\
                    key not in self.cache_data.keys():
                print('DISCARD: {}'.format(self.lastkey))
                del self.cache_data[self.lastkey]
            self.cache_data[key] = item
            self.lastkey = key

    def get(self, key):
        """ get items from dict"""
        if key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
