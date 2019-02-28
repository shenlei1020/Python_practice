#! /usr/bin/env python
# -*- coding: utf-8 -*-

# link: https://www.nowcoder.com/test/question/done?tid=21241453&qid=147541#summary

def arrange_id(len_id, id_str):
    """
    :param len_id:
    :param id_str:
    :return:
    """
    id_list = id_str.split(" ")
    result = []
    for i in range(len_id):
        if id_list[i] in result:
            result.pop(result.index(id_list[i]))
        result.insert(0, id_list[i])
    re_str = ' '.join(result)
    return re_str


if __name__ == "__main__":
    eventNum = int(input())
    for i in range(eventNum):
        len_id = int(input())
        id_str = input()
        print("%s" % arrange_id(len_id,id_str))
