# -*- coding:utf-8 -*-

"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

"""

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
            
            data_lenth = len(numbers)
            return_num = 0
            if data_lenth % 2 != 0:
                data_lenth = (data_lenth -1) / 2
            times ={}
            for i in numbers:
                if i in times.keys():
                    times[i] += 1
                else:
                    times[i] = 1
            for k, v in times.items():
                #print(v,data_lenth)
                if v > data_lenth:
                    return_num = k
            return return_num
