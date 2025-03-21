# Problem: Max Number of K-Sum Pairs - https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        nums.sort()
        left = 0
        right = len(nums) - 1
        count = 0
        
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == k:
                count += 1
                left += 1
                right -= 1
            elif current_sum < k:
                left += 1
            else:
                right -= 1
        
        return count