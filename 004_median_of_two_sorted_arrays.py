class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)

        if len1 < len2:
            start = 0
            end = len1
            while start < end:
                mid1 = (start + end) // 2
                mid2 = (len1 + len2 + 1)//2 - mid1
                if mid1 - 1 >= 0 and mid1 - 1 < len1 and mid2 >= 0 and mid2 < len2 and nums1[mid1-1] > nums2[mid2]:
                    end = mid1
                    continue
                elif mid1 >= 0 and mid1 < len1 and mid2 - 1 >= 0 and mid2 - 1 < len2 and nums1[mid1] < nums2[mid2-1]:
                    start = mid1 + 1
                    continue
                else:
                    if (len1 + len2) % 2:
                        if mid1 - 1 >= 0 and mid1 - 1 < len1 and mid2 - 1 >= 0 and mid2 - 1 < len2:
                            return max(nums1[mid1 - 1], nums2[mid2 - 1])
                        elif mid1 - 1 >= 0 and mid1 - 1 < len1:
                            return nums1[mid1 - 1]
                        elif mid2 - 1 >= 0 and mid2 - 1 < len2:
                            return nums2[mid2 - 1]
                    else:
                        return (max(nums1[mid1 - 1], nums2[mid2 - 1]) + min(nums1[mid1], nums2[mid2])) / 2

            if start == end:
                mid1 = start
                mid2 = (len1 + len2 + 1) // 2 - mid1
                if (len1 + len2) % 2:
                    return nums2[mid2 - 1]
                else:
                    return (nums2[mid2 - 1] + nums2[mid2]) / 2
        else:
            start = 0
            end = len2
            while start < end:
                mid2 = (start + end) // 2
                mid1 = (len1 + len2 + 1) // 2 - mid2
                if nums1[mid1 - 1] > nums2[mid2]:
                    end = mid2
                elif nums1[mid1] < nums2[mid2 - 1]:
                    start = mid2 + 1
                else:
                    if (len1 + len2) % 2:
                        return max(nums1[mid1 - 1], nums2[mid2 - 1])
                    else:
                        return (max(nums1[mid1 - 1], nums2[mid2 - 1]) + min(nums1[mid1], nums2[mid2])) / 2
            if start == end:
                mid2 = start
                mid1 = (len1 + len2 + 1) // 2 - mid2
                if (len1 + len2) % 2:
                    return nums1[mid1 - 1]
                else:
                    return (nums1[mid1 - 1] + nums1[mid1]) / 2


if __name__ == "__main__":
    nums1 = [3]
    nums2 = [1,2,2]
    print(Solution.findMedianSortedArrays(None, nums1,nums2))
