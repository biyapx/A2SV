# Problem:  Longest Square Streak in an Array - https://leetcode.com/problems/longest-square-streak-in-an-array/description/?envType=problem-list-v2&envId=sorting

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        num_set = set(nums)
        maxx = 0
        
        for num in sorted(nums):
            current = num
            streak = 1
            
            while current * current in num_set:
                current = current * current
                streak += 1
            
            maxx = max(maxx, streak)
        
        return maxx if maxx >= 2 else -1