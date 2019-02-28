#! /usr/bin/env python
# -*- coding: utf-8 -*-

# link: https://www.nowcoder.com/test/question/done?tid=21241453&qid=117516#summary

def search_word(m, n, plane, word):
    """
    :param m:
    :param n:
    :param plane:
    :param word:
    :return:
    """
    countNum = 0
    len_w = len(word)
    for i in range(m):  # horizontal
        for j in range(n-len_w+1):
            if plane[i][j:(j+len_w)] == word:
                countNum += 1
    for x in range(m-len_w+1):
        for y in range(n):
            for lw in range(len_w):
                if plane[x+lw][y] != word[lw]:
                    break
                if lw == (len_w-1):
                    countNum += 1

    for k in range(m-len_w+1):
        for l in range(n-len_w+1):
            for lw in range(len_w):
                if plane[k+lw][l+lw] != word[lw]:
                    break
                if lw == (len_w-1):
                    countNum += 1
    return countNum


if __name__ == "__main__":
    eventNum = int(input())  # total event number
    for i in range(eventNum):
        input1 = input().split(' ')  # numbers of row and column e.g. 5 8
        m = int(input1[0])
        n = int(input1[1])
        plane = []
        for j in range(m):
            plane.append(input())
        word = input()
        print(search_word(m, n, plane, word))
