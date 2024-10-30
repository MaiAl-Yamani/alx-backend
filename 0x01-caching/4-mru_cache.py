#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """A class LRUCache that inherits from BaseCaching."""

    def __init__(self):
        """Initialize the LRUCache."""
        super().__init__()
        self.ac_cnt = {}

    def put(self, key, item):
        """Add item function"""
        if key is not None and item is not None:
            sorted_keys =\
                sorted(self.ac_cnt, key=lambda k: self.ac_cnt[k], reverse=True)
            discarded_key = None
            if len(self.cache_data) ==\
                    self.MAX_ITEMS and key not in self.cache_data.keys():
                discarded_key = sorted_keys[0]
                self.ac_cnt[key] = self.ac_cnt[discarded_key] + 1
                print('DISCARD: {}'.format(discarded_key))
                del self.cache_data[discarded_key]
                del self.ac_cnt[discarded_key]
            if len(self.ac_cnt) == 0:
                self.ac_cnt[key] = 1
            elif len(self.cache_data) < self.MAX_ITEMS:
                key_with_largest_value =\
                    max(self.ac_cnt, key=lambda k: self.ac_cnt[k])
                self.ac_cnt[key] =\
                    self.ac_cnt[key_with_largest_value] + 1

            self.cache_data[key] = item

    def get(self, key):
        """Get function"""
        if key in self.cache_data.keys():
            if len(self.ac_cnt) == 0:
                self.ac_cnt[key] = 1
            else:
                key_with_largest_value =\
                    max(self.ac_cnt, key=lambda k: self.ac_cnt[k])
                self.ac_cnt[key] = self.ac_cnt[key_with_largest_value] + 1
            return self.cache_data[key]
        else:
            return None
