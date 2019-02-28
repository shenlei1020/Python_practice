#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time


def sequence_arrange(n):
    """
    :param n: number
    :return: draw a "Y"
    """
    if (n % 3 != 1) or (n < 4):
        print("The input number is wrong(3*k+1)!")
        return -1
    branch = (n - 1) // 3
    rowNum = 2 * branch + 1
    result = ['x']
    for i in range(branch):
        result = ['-'+j for j in result]
        result.append(result[-1])
        result.insert(0, ('x'+(2*i+1)*'-'+'x'))
    for i in range(rowNum):
        print("%s\n" % result[i])
    return 1


def sequence_arrange_v1(n):
    """
    :param n: number
    :return: draw a "Y"
    """
    if (n % 3 != 1) or (n < 4):
        print("The input is wrong(3*k+1)!")
        return -1
    branch = (n - 1) // 3
    # totNum = 2 * branch + 1
    result = 'x' + (2 * branch - 1)*'-' + 'x'
    print("%s\n" % result)
    for i in range(branch):
        result = '-'+result[0:-3]+'x'
        print("%s\n" % result)
    for i in range(branch):
        print("%s\n" % result)
    return 1


if __name__ == "__main__":
    startT = time.clock()
    sequence_arrange_v1(10000*3+1)
    stopT = time.clock()
    print("Cost time %s" % str(stopT-startT))
