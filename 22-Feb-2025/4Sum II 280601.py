# Problem: 4Sum II - https://leetcode.com/problems/4sum-ii/

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        sum_map = {}
        
        for n1 in nums1:
            for n2 in nums2:
                sum_map[n1 + n2] = sum_map.get(n1 + n2, 0) + 1
        
        for n3 in nums3:
            for n4 in nums4:
                target = -(n3 + n4)
                count += sum_map.get(target, 0)
        
        return count