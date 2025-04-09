# Problem: Reduction Operations to Make the Array Elements Equal - LeetCode - https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/description/

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        operations = 0
        unique_count = 0

        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                unique_count += 1
            operations += unique_count

        return operations
