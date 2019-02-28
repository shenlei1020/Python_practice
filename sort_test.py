#! /usr/bin/env python
# coding: utf-8


def bubble_sort(mylst):
    """
    :param mylst:
    :return:
    """
    flag = True
    label = 0
    lenlst = len(mylst)
    while (flag):
        flag = False
        for i in range(1, lenlst-label):
            if mylst[i] < mylst[i-1]:
                mylst[i], mylst[i-1] = mylst[i-1], mylst[i]
                flag = True
        label += 1
    return mylst


def select_sort(mylst):
    """
    :param mylst:
    :return:
    """
    lenlst = len(mylst)
    L = 0
    while L < lenlst - 1:
        temp_id = L
        for i in range(L, lenlst-1):
            if mylst[temp_id] > mylst[i+1]:
                temp_id = i + 1
        mylst[temp_id], mylst[L] = mylst[L], mylst[temp_id]
        L += 1
    return mylst


def insert_sort(mylst):
    """
    :param mylst:
    :return:
    """
    lenlst = len(mylst)
    for i in range(1, lenlst):
        j = i - 1
        while mylst[j] > mylst[j+1] and j >= 0:
            mylst[j], mylst[j+1] = mylst[j+1], mylst[j]
            j -= 1
    return mylst


def merge_sort(mylst):
    """
    :param mylst:
    :return:
    """
    def merge(lst1, lst2):
        """
        :param midlst:
        :return:
        """
        lenlst1 = len(lst1)
        lenlst2 = len(lst2)
        result = []
        lenlst = lenlst1 + lenlst2
        if not lst1:
            return lst2
        elif not lst2:
            return lst1
        for i in range(lenlst):
            if lst1[0] < lst2[0]:
                result.append(lst1[0])
                del lst1[0]
            else:
                result.append(lst2[0])
                del lst2[0]
            if not lst1:
                result += lst2
                return result
            elif not lst2:
                result += lst1
                return result
        return result
    lenlst = len(mylst)
    mid = lenlst // 2
    if lenlst == 2:
        if mylst[0] > mylst[1]:
            mylst[0], mylst[1] = mylst[1], mylst[0]
        return mylst
    if lenlst > 2:
        mylst1 = merge_sort(mylst[:mid])
        mylst2 = merge_sort(mylst[mid:])
        mylst = merge(mylst1, mylst2)
    return mylst


if __name__ == "__main__":
    mylst = input().split()
    mylst = list(map(int, mylst))
    outlst = merge_sort(mylst)
    outlst = ' '.join(list(map(str, outlst)))
    print(outlst)