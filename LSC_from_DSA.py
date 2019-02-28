#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
Author: Lei Shen
Date: 20190226
"""
from time import clock
import numpy as np


def lsc(A, B):
    """
    :param A:
    :param B:
    :return:
    """
    lenA = len(A)
    lenB = len(B)
    C = np.matrix((lenA+1)*[(lenB+1)*[0]])
    for i in range(1, lenA+1):
        for j in range(1, lenB+1):
            if A[i-1] == B[j-1]:
                C[i, j] = C[i-1, j-1] + 1
            else:
                C[i, j] = max(C[i-1, j], C[i, j-1])
    max_count = C[lenA, lenB]
    tempA = lenA
    tempB = lenB
    restr = ""
    while max_count > 0:
        loc = np.where(C[:tempA+1, :tempB+1] == max_count)
        tempA = loc[0][0]
        tempB = loc[1][0]
        restr = A[tempA-1] + restr
        max_count -= 1
    return restr


def find_max(C):
    if len(C) == 1:
        return C[0]
    return max(find_max(C[:1]), find_max(C[1:]))


if __name__ == "__main__":
    A = "qwertyuiopasdfghjklzxcvbnm"
    B = "jhgfdsaqmwnebrvtcyxuzilokp"
    C = list(range(500))
    start = clock()
    print(lsc(A, B))
    print("Cost time: %f" % (clock()-start))
