# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        a = 0
        b = 1
        if n == 0:
            return a
        elif n == 1:
            return b
        elif n == 2:
            return b
        else:
            for i in range(n):
                a,b = b,a
                b = a + b
            return a 
