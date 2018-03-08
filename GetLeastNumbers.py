# -*- coding:utf-8 -*-

"""
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
"""

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k > len(tinput):
            return []
        else:
            for i in range(len(tinput)-1,0,-1):
                for o in range(i):
                    if tinput[o] > tinput[o+1]:
                        tinput[o],tinput[o+1] = tinput[o+1],tinput[o]
            return tinput[0:k]
    
