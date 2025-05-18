# Problem: Intersection of Two Arrays II - https://leetcode.com/problems/intersection-of-two-arrays-ii/


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapp1 = Counter(nums1)
        mapp2 = Counter(nums2)
        res = []
        for i in set(mapp1):
            if i in mapp2:
                res+= [i] * min(mapp1[i], mapp2[i])
        return res