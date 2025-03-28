# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        reminderIndex = {0: -1}
        total = 0
        for index, num in enumerate(nums):
            total += num
            reminder = total % k
            if reminder not in reminderIndex:
                reminderIndex[reminder] = index
            elif index - reminderIndex[reminder] > 1:
                return True
        return False