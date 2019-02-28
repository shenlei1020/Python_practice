#!/usr/bin/env python
# -*- coding: utf-8 -*-


def power_calc(mylst):
    """
    :param mylst: input pars
    :return: total power
    """
    N = mylst[0]
    K = mylst[1]
    tempx = mylst[2]
    tempy = mylst[3]
    C = mylst[4]
    D = mylst[5]
    E1 = mylst[6]
    E2 = mylst[7]
    F = mylst[8]
    A = [(tempx + tempy) % F]
    # calculate array A.
    for i in range(1, N):
        x = (C * tempx + D * tempy + E1) % F
        y = (D * tempx + C * tempy + E2) % F
        tempx, tempy = x, y
        A.append((x+y) % F)
    # calculate power
    temp = A[-1]
    Alst = [temp]
    for i in range(2, N + 1):
        temp += A[-i] * i
        Alst.insert(0, temp)
    result = Alst[0] * K
    for j in range(2, N + 1):
        result += Alst[j - 1] * j * (j ** K - 1) // (j - 1)
    return result


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        mylst = input().split()
        mylst = list(map(int, mylst))
        tot_power = power_calc(mylst) % 1000000007
        print("Case #%d: %d" % (i + 1, tot_power))
