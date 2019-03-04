#!/usr/bin/python
# -*- coding: utf-8 -*-


def stack_permutation(olst, ilst):
    temp = []
    lenolst = len(olst)
    while olst:
        if (not temp) or olst[0] != temp[-1]:
            if olst[0] in ilst:
                while olst[0] != ilst[-1]:
                    temp.append(ilst.pop())
                del olst[0]
                ilst.pop()
            else:
                return False
        else:
            del olst[0]
            temp.pop()
    return True


if __name__ == "__main__":
    ilst = [9, 8, 7, 6, 5, 4, 3, 2, 1]  # , 5, 6, 7, 8, 9
    olst = [3, 2, 1, 4, 5, 7, 6, 9, 8]  #
    print("The stack permutation is: ", stack_permutation(olst, ilst))

