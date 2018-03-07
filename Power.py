# -*- coding:utf-8 -*-

"""
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
"""

class Solution:
    def Power(self, base, exponent):
        # write code here
        total = base
        if exponent == 1:
            return base
        elif exponent == 0:
            return 1 
        elif exponent < 0:
            for i in range(abs(exponent)-1):
                base = base * total
            return 1 / base
        else:
            for i in range(exponent-1):
                base = base * total 
            return base
        
