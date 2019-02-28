#! /usr/bin/env python
# -*- coding: utf-8 -*-

# sheep_walking link: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050fc5/0000000000054edd

from time import clock

def herd_sheep(X, Y, my_dict):
    """
    :param X:
    :param Y:
    :return:
    """
    if (X, Y) in my_dict:
        return my_dict[(X, Y)], my_dict
    if X == 0 and Y == 0:
        return 0, my_dict
    if X == 0 and Y != 0:
        return herd_sheep(0, Y-1, my_dict)[0] * 2/3 + herd_sheep(1, Y-1, my_dict)[0]/3 + 2, my_dict
    if X != 0 and Y != 0:
        if X == Y:
            return herd_sheep(X - 1, Y, my_dict)[0] + 1, my_dict
        else:
            return herd_sheep(X - 1, Y, my_dict)[0] / 2 + herd_sheep(X, Y - 1, my_dict)[0] / 2 + 1, my_dict


def steps(X, Y, my_dict):
    y = 0
    if Y == 0:
        return 0, my_dict
    while y < Y:
        y += 1
        for i in range(y+1):
            my_dict[(i, y)], my_dict = herd_sheep(i, y, my_dict)
            if i == X and y == Y:
                return my_dict[(i, y)], my_dict
            if i == X:  # selected the needed area to calculate
                break


if __name__ == "__main__":
    totNum = int(input())
    my_dict = {(0, 0): 0, (0, 1): 3}
    for i in range(totNum):
        input_coor = input().split(" ")
        coordinates = list(map(int, input_coor))
        start_t = clock()
        X = abs(coordinates[0])
        Y = abs(coordinates[1])
        if X > Y:  # transfer to 1/8 area, X < Y
            X, Y = Y, X
        result, my_dict = steps(X, Y, my_dict)
        print("Case #%d: %.6f" % (i+1, result))
        print("Cost time: %.9f" % (clock()-start_t))
