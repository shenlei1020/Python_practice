#! /usr/bin/env python
# -*- coding: utf-8 -*-


def snake_escape(R, C, K):
    """
    :param R:
    :param C:
    :param K:
    :return:
    """
    if K == (R * C - 1):
        return "IMPOSSIBLE", ""
    if C == 1:
        escape_1 = R * ['N']
        if K != R:
            escape_1[K] = "S"
        return "POSSIBLE", escape_1
    rowNum = K // C
    moreNum = K % C
    escape = rowNum * [C * 'W']
    if moreNum == (C - 1):
        escape.append(moreNum*"W" + "S")
    elif moreNum == 0:
        escape.append("E" + (C - 1)*"W")
    elif rowNum == (R - 1):
        escape.append(moreNum * "W" + "E" + (C - moreNum - 1) * "W")
    else:
        escape.append(moreNum * "W" + "S" + (C - moreNum - 1) * "W")
    for i in range(rowNum+1, R):
        escape.append("E" + (C - 1) * "W")
    return "POSSIBLE", escape


if __name__ == "__main__":
    totNum = int(input())
    for i in range(totNum):
        args = input().split(" ")
        myresult, mypath = snake_escape(int(args[0]), int(args[1]), int(args[2]))
        print("Case #%d: %s" % (i+1, myresult))
        if myresult == "POSSIBLE":
            for j in range(int(args[0])):
                print(mypath[j])
