# Problem: Merge Sorted Array
(Easy) - https://leetcode.com/problems/merge-sorted-array/

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m - 1, n - 1
        pos = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[pos] = nums1[p1]
                p1 -= 1
            else:
                nums1[pos] = nums2[p2]
                p2 -= 1
            pos -= 1
        while p2 >= 0:
            nums1[pos] = nums2[p2]
            p2 -= 1
            pos -= 1
