#!/usr/bin/env python
# -*- coding: utf-8 =*-

from math import floor


def bin_search_b(nums, target):
        # write your code here
        if not nums or target is None: # 先判断传给我们的数据是否为空，如果是空的话直接返回-1。如果不判断的话在后面会报错。
            return -1
 
        start = 0
        end = len(nums)
 
        while start < end:
            mid = (start + end) // 2
            if target < nums[mid]:
                end = mid
            else:
                start = mid + 1  # 不能直接返回，不然找的的不一定是最后一个

        return start - 1  # 这里一定是先判断end， 因为要找的是最后一个



def interplation_search(nums, target):
    """
    :param nums:
    :param target:
    :return:
    """
    lens = len(nums)
    lo = 0
    hi = lens - 1
    while lo < hi:
        mid = lo + floor((hi - lo) * ((target - nums[lo])/(nums[hi] - nums[lo])))
        if mid < lo:
            return -1
        if mid > hi:
            return -1
        if target < nums[mid]:
            hi = mid - 1
        elif target > nums[mid]:
            lo = mid + 1
        else:
            return mid
    return -1


if __name__ == "__main__":
    """
    利用二分查找，找到有序数组nums中的特定target的最后的位置。
    """
    nums = [1, 2, 2, 3, 5, 6, 6, 6, 7, 8, 9]
    target = 6
    print(bin_search_b(nums, target))
