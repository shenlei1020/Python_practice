#! /usr/bin/env python
# -*- coding: utf-8 -*-


def divide_land(K, mark_lst):
    """
    :param K: 5
    :param mark_lst: 7 8 7 6 5 6
    :return: 1
    """
    addNum = 0
    flag = []
    for i in range(1, K+1):
        if mark_lst[i] > mark_lst[i-1]:
            flag.append(1)
        elif mark_lst[i] < mark_lst[i-1]:
            flag.append(-1)
    last_v = flag[0]
    for j in range(1, len(flag)):
        if last_v * flag[j] < 0:
            addNum += 1
            if (j+1) < len(flag):
                last_v = flag[j+1]
    return addNum-1


if __name__ == "__main__":
    totNum = int(input())
    for i in range(totNum):
        K = int(input())
        marks = input().split(" ")
        mark_lst = list(map(int, marks))
        print("Case #%d: %s" % (i+1, divide_land(K, mark_lst)))
