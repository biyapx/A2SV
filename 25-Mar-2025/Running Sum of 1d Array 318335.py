# Problem: Running Sum of 1d Array - https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = [0] * len(nums)
        runningSum[0] = nums[0]
        
        for i in range(1, len(nums)):
            runningSum[i] = runningSum[i - 1] + nums[i]
        
        return runningSum