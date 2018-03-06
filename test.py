#!/usr/bin/env python
# coding:utf-8
# Created by jihaojie at 2018/2/24


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0

        for i in range(len(rotateArray)-1):
            print(i)
            #print(rotateArray[i],rotateArray[i+1])
            if rotateArray[i] < rotateArray[i+1]:
                print(rotateArray[i])
                rotateArray[i], rotateArray[i+1] = rotateArray[i + 1], rotateArray[i]

        return rotateArray[-1]


