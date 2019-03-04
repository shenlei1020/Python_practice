#!/usr/bin/python
# -*- coding: utf-8 -*-


def hannuota(n, i, j, num):
    x = i % 3
    y = j % 3
    if n == 1:
        print("%d -> %d" % (x, y))
        num += 1
        return num
    num = hannuota(n - 1, x, 3 - x - y, num)
    print("%d -> %d" % (x, y))
    num += 1
    num = hannuota(n - 1, 3 - x - y, y, num)
    return num


if __name__ == "__main__":
    num = hannuota(10, 0, 2, 0)
    print("Total steps: %d" % num)

