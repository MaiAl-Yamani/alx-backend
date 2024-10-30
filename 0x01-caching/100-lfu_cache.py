#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """A class LRUCache that inherits from BaseCaching."""

    def __init__(self):
        """Initialize the LRUCache."""
        super().__init__()
        self.ac_cnt = {}

    def put(self, key, item):
        """Add items function"""
        discarded_key = None
        if key is not None and item is not None:
            if key in self.ac_cnt:
                sorted_keys =\
                    sorted(self.ac_cnt, key=lambda k: self.ac_cnt[k])
                discarded_key = sorted_keys[0]
                self.ac_cnt[key] = self.ac_cnt[key] + 1
            else:
                if len(self.cache_data) == self.MAX_ITEMS:
                    sorted_keys =\
                        sorted(self.ac_cnt, key=lambda k: self.ac_cnt[k])
                    discarded_key = sorted_keys[0]
                self.ac_cnt[key] = 0

            if len(self.cache_data) ==\
                    self.MAX_ITEMS and key not in self.cache_data.keys():
                print('DISCARD: {}'.format(discarded_key))
                del self.cache_data[discarded_key]
                del self.ac_cnt[discarded_key]

            self.cache_data[key] = item

    def get(self, key):
        """Get items function"""
        if key in self.cache_data.keys():
            if key not in self.ac_cnt:
                self.ac_cnt[key] = 0
            else:
                self.ac_cnt[key] = self.ac_cnt[key] + 1
            return self.cache_data[key]
        else:
            return None
