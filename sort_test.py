#! /usr/bin/env python
# coding: utf-8


from time import clock


def bubble_sort(mylst):
    """
    :param mylst:
    :return:
    """
    flag = False
    last = len(mylst)
    while not flag:
        flag = True
        for i in range(1, last):
            if mylst[i] < mylst[i-1]:
                mylst[i], mylst[i-1] = mylst[i-1], mylst[i]
                last = i
                flag = False
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
        j = i
        while j > 0 and mylst[j-1] > mylst[j]:
            mylst[j], mylst[j-1] = mylst[j-1], mylst[j]
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
        if not lst1:
            return lst2
        elif not lst2:
            return lst1
        i = 0
        j = 0
        while i < lenlst1 or j < lenlst2:
            if i < lenlst1 and (j >= lenlst2 or lst1[i] <= lst2[j]):
                result.append(lst1[i])
                i += 1
            if j < lenlst2 and (i >= lenlst1 or lst1[i] > lst2[j]):
                result.append(lst2[j])
                j += 1
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

    mylst = "30 28 29 22 24 23 25 19 21 20 18 15 16 17 14 11 12 13 9 10 7 8 6 4 5 3 2 1 30 28 29 22 24 23 25 19 21 20 18 15 16 17 14 11 12 13 9 10 7 8 6 4 5 3 2 1 30 28 29 22 24 23 25 19 21 20 18 15 16 17 14 11 12 13 9 10 7 8 6 4 5 3 2 1 30 28 29 22 24 23 25 19 21 20 18 15 16 17 14 11 12 13 9 10 7 8 6 4 5 3 2 1 30 28 29 22 24 23 25 19 21 20 18 15 16 17 14 11 12 13 9 10 7 8 6 4 5 3 2 1 30 28 29 22 24 23 25 19 21 20 18 15 16 17 14 11 12 13 9 10 7 8 6 4 5 3 2 1 30 28 29 22 24 23 25 19 21 20 18 15 16 17 14 11 12 13 9 10 7 8 6 4 5 3 2 1 30 28 29 22 24 23 25 19 21 20 18 15 16 17 14 11 12 13 9 10 7 8 6 4 5 3 2 1 30 28 29 22 24 23 25 19 21 20 18 15 16 17 14 11 12 13 9 10 7 8 6 4 5 3 2 1 30 28 29 22 24 23 25 19 21 20 18 15 16 17 14 11 12 13 9 10 7 8 6 4 5 3 2 1 30 28 29 22 24 23 25 19 21 20 18 15 16 17 14 11 12 13 9 10 7 8 6 4 5 3 2 1 30 28 29 22 24 23 25 19 21 20 18 15 16 17 14 11 12 13 9 10 7 8 6 4 5 3 2 1"
    mylst = mylst.split()
    mylst = list(map(int, mylst))
    start = clock()
    outlst = insert_sort(mylst)
    outlst = ' '.join(list(map(str, outlst)))
    print(outlst)
    print("Cost time: %f" % (clock() - start))