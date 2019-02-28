#! /usr/bin/env python
# -*- coding: utf-8 -*-

#  link: https://www.nowcoder.com/test/question/done?tid=21241453&qid=117506#summary

def check_time(time_str):
    """
    :param time_str:'33:33:33'
    :return:
    """
    input_t = time_str.split(':')
    temp_t = list(map(int, input_t))
    result = time_str
    if temp_t[0] > 23:
        result = '0' + result[1:]
    if temp_t[1] > 59:
        result = result[:3]+'0'+result[4:]
    if temp_t[2] > 59:
        result = result[:6]+'0'+result[7]
    return result


if __name__ == "__main__":
    totNum = int(input())
    for i in range(totNum):
        input_arg = input()
        print("%s\n" % check_time(input_arg))
