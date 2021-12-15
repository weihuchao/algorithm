#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self._data = {}
        self._queque = []
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self._data:
            self._queque.remove(key)
            self._queque.append(key)
            return self._data[key]
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.get(key) == -1:
            self._data[key] = value
            if len(self._queque) == self.capacity:
                remove_key = self._queque.pop(0)
                del self._data[remove_key]
            self._queque.append(key)
        else:
            self._data[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
