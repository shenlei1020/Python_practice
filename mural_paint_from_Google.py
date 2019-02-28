#!/usr/bin/env python
# -*- coding: utf-8 -*-


def mural_paint(N, wall):
    """
    :param N:
    :param wall:
    :return:
    """
    start = (N + 1) // 2
    tempMax = sum(wall[0:start])
    result = tempMax
    for i in range(start, N):
        tempMax += (wall[i] - wall[i - start])
        result = max(result, tempMax)
    return result


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N = int(input())
        wall = list(map(int, input()))
        score = mural_paint(N, wall)
        print("Case #%d: %d" % (i+1, score))