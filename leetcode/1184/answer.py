#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao
class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        ret = []
        n = len(distance)
        for s, d in [(start, destination), (destination, start)]:
            r = 0
            while s != d:
                r += distance[s]
                s += 1
                s = s % n
            ret.append(r)
        return min(ret)
