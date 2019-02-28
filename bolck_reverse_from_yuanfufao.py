#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import numpy as np


def reverse_sequence(input1, input2):
    """
    :param input1: A str contains two numbers. The first is  total number and the second is car size.
    :param input2: A str contains the sequence.
    :return: Return the block reversed sequence.
    """
    input_arg = input1.split(' ')
    sequ = input2.split(' ')
    totNum = int(input_arg[0])
    eachCar = int(input_arg[1])
    result = []
    if totNum != len(sequ):
        print("The input is wrong!")
        return "Error!"
    hId = totNum - (totNum % eachCar)
    if hId == totNum:
        hId -= eachCar
    reId = hId
    while reId >= 0:
        result.append(sequ[reId])
        reId += 1
        if (reId % eachCar == 0) or (reId >= totNum):
            hId -= eachCar
            reId = hId
    result_re = ' '.join(result)
    return result_re


if __name__ == "__main__":
    input1 = input("Total number and car number:\n")  # 9 4
    input2 = input("The original sequence:\n")  # 2 3 1 5 4 6 8 7 9
    # input1 = "100 15"
    # input2 = np.arange(100)
    # np.random.shuffle(input2)
    # input2 = ' '.join(map(str, input2))
    start_t = time.clock()
    result = reverse_sequence(input1, input2)
    stop_t = time.clock()
    print("Reverse sequence: %s" % result)
    print("Cost time: %s" % str(stop_t-start_t))
