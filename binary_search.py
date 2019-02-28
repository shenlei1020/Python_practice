class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):
        # write your code here
        if not nums:
            return -1
        first_loc = 0
        last_loc = len(nums)-1
        mid_loc = last_loc//2
        while first_loc+1 < last_loc:
            if target == nums[mid_loc]:
                first_loc = mid_loc
            elif target > nums[mid_loc]:
                first_loc = mid_loc
            else:
                last_loc = mid_loc
            mid_loc = (first_loc + last_loc) // 2
        if target == nums[last_loc]:
            return last_loc
        elif target == nums[first_loc]:
            return first_loc
        else:
            return -1


def lastPosition(self, nums, target):
        # write your code here
        if not nums or target is None: # 先判断传给我们的数据是否为空，如果是空的话直接返回-1。如果不判断的话在后面会报错。
            return -1
 
        start = -1
        end = len(nums)
 
        while start + 1 < end:
            mid = (start + end) // 2
            if target < nums[mid]:
                end = mid
            else:
                start = mid  # 不能直接返回，不然找的的不一定是最后一个
        if nums[start] == target:  # 这里一定是先判断end， 因为要找的是最后一个
            return start
        else:
            return -1


if __name__ == "__main__":
    """
    利用二分查找，找到有序数组nums中的特定target的最后的位置。
    """
    nums = [1,2,2,3,3,3,5,5,5,7,8,8,8,9,9]
    target = 0
    print(lastPosition(-1,nums,target))