#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: Lei Shen
Date: 2019/02/27
"""


def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    ss = "#"
    for i in s:
        ss += i + "#"
    lenss = len(ss)
    p = lenss * [1]
    midId = 0
    rightId = 0
    for i in range(lenss):
        if i < rightId:
            p[i] = min(p[2 * midId - i], rightId - i)
        while i-p[i] >= 0 and i+p[i] < lenss and ss[i-p[i]] == ss[i+p[i]]:
            p[i] += 1
        if i+p[i] > rightId:
            midId = i
            rightId = i + p[i]
    maxId = max(p)
    maxindex = p.index(maxId)
    result = ss[maxindex - maxId + 2:maxId + maxindex:2]
    return result


if __name__ == "__main__":
    s = input()
    result = longestPalindrome(s)
    print(result)
