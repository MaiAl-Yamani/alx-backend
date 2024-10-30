#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Create a class LRUCache that inherits from BaseCaching."""

    def __init__(self):
        """Initialize the LRUCache."""
        super().__init__()
        self.access_count = {}

    def put(self, key, item):
        """Add items to the cache."""
        if key is not None and item is not None:
            if len(self.access_count) == 0:
                self.access_count[key] = 1
            else:
                key_with_largest_value =\
                    max(self.access_count, key=lambda k: self.access_count[k])
                self.access_count[key] =\
                    self.access_count[key_with_largest_value] + 1

            # Sort keys based on access count
            sorted_keys =\
                sorted(self.access_count, key=lambda k: self.access_count[k])

            # Discard the least recently used item if cache is full
            if len(self.cache_data) ==\
                    self.MAX_ITEMS and key not in self.cache_data.keys():
                discarded_key = sorted_keys[0]
                print('DISCARD: {}'.format(discarded_key))
                del self.cache_data[discarded_key]
                del self.access_count[discarded_key]

            self.cache_data[key] = item

    def get(self, key):
        """Get items from the cache."""
        if key in self.cache_data.keys():
            if len(self.access_count) == 0:
                self.access_count[key] = 1
            else:
                key_with_largest_value =\
                    max(self.access_count, key=lambda k: self.access_count[k])
                self.access_count[key] =\
                    self.access_count[key_with_largest_value] + 1
            return self.cache_data[key]
        else:
            return None
