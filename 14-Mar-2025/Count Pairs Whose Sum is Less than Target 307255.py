# Problem: Count Pairs Whose Sum is Less than Target - https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort() 
        count = 0
        n = len(nums)
        
        for i in range(n):
            j = i + 1
            while j < n and nums[i] + nums[j] < target:
                count += 1
                j += 1
                
        return count