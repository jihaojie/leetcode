# -*- coding:utf-8 -*-

"""
连续子数组的最大和
"""
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        max_num = array[0]
        for i in range(len(array)):
            cache_num = 0
            for o in range(i,len(array)):
                cache_num += array[o]
                if cache_num > max_num:
                    max_num = cache_num
        return max_num
