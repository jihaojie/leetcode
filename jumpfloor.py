# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        a = 1
        b = 2
        if number <= 2:
            return number
        else:
            for i in range(number-2):
                a,b = b,a
                b = a + b 
        return b 
                
            
