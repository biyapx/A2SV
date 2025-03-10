# Problem: Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_set = sorted(set(nums))
        for i in range(len(nums_set)):
            nums[i] = nums_set[i]
        return len(nums_set)
