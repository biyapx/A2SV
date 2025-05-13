# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

from typing import List

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        diff = [0] * (n + 1)
        
        for start, end in requests:
            diff[start] += 1
            if end + 1 < n:
                diff[end + 1] -= 1
        
        freq = [0] * n
        current = 0
        for i in range(n):
            current += diff[i]
            freq[i] = current
        
        freq.sort(reverse=True)
        nums.sort(reverse=True)
        
        max_sum = 0
        for i in range(n):
            max_sum += freq[i] * nums[i]
        
        return max_sum % MOD