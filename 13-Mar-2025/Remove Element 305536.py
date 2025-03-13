# Problem: Remove Element - https://leetcode.com/problems/remove-element/description/

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if val == []:
            return 0
        else:
            i = 0
            j = 0
            while j < len(nums):
                if nums[j] == val:
                    j += 1
                else:
                    nums[i] = nums[j]
                    i += 1
                    j += 1
            return len(nums[0:i])